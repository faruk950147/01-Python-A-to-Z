from django.db import models, transaction
from django.utils import timezone
from django.utils.timezone import localtime
from django.core.validators import RegexValidator, FileExtensionValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from datetime import timedelta
import uuid
import re
import logging

logger = logging.getLogger(__name__)


# =========================================================
# CONFIG
# =========================================================
ONLINE_TIMEOUT_SECONDS = 60
LAST_SEEN_UPDATE_INTERVAL = 30

ACCOUNT_LOCK_MINUTES = 15
MAX_FAILED_ATTEMPTS = 5

EMAIL_TOKEN_EXPIRE_HOURS = 24
RESET_TOKEN_EXPIRE_HOURS = 1

# Password policy
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128


# =========================================================
# VALIDATORS
# =========================================================
phone_validator = RegexValidator(
    r"^\+?\d{10,15}$",
    "Enter a valid phone number"
)

username_validator = UnicodeUsernameValidator()

def validate_password_strength(password):
    """Password strength validation"""
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValidationError(
            _("Password must be at least %(min_length)d characters"),
            params={'min_length': MIN_PASSWORD_LENGTH}
        )
    if not re.search(r"[A-Z]", password):
        raise ValidationError(_("Password must contain at least one uppercase letter"))
    if not re.search(r"[a-z]", password):
        raise ValidationError(_("Password must contain at least one lowercase letter"))
    if not re.search(r"[0-9]", password):
        raise ValidationError(_("Password must contain at least one number"))
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError(_("Password must contain at least one special character"))
    return password


# =========================================================
# PHONE NORMALIZER
# =========================================================
def normalize_phone_number(phone):
    if not phone:
        return None
    
    phone = re.sub(r"\s+", "", phone)
    phone = re.sub(r"-+", "", phone)
    
    if phone.startswith("+880"):
        normalized = phone
    elif phone.startswith("880"):
        normalized = "+" + phone
    elif phone.startswith("01"):
        normalized = "+880" + phone[1:]
    else:
        return None
    
    # BANGLADESH PHONE NUMBER LENGTH IS 13 (+880 + 11 digits)
    if len(normalized) != 13:
        return None
    
    # MANIFEST NUMBER CHECK (017, 018, 019 starts)
    if not normalized.startswith("+8801") or normalized[5] not in ['7', '8', '9']:
        # 013, 014, 015, 016 also currently used
        if normalized[5] not in ['3', '4', '5', '6', '7', '8', '9']:
            return None
    
    return normalized


# =========================================================
# USER MANAGER
# =========================================================
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, phone, password, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required")
        if not phone:
            raise ValueError("Phone is required")

        phone = normalize_phone_number(phone)
        if not phone:
            raise ValidationError({"phone": "Invalid Bangladeshi phone number"})

        user = self.model(
            username=username.strip().lower(),
            email=self.normalize_email(email).strip().lower(),
            phone=phone,
            **extra_fields
        )

        #Password validation
        if password:
            validate_password_strength(password)
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.save(using=self._db)
        return user

    def create_user(self, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_verified", False)
        
        return self._create_user(username, email, phone, password, **extra_fields)

    def create_superuser(self, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(username, email, phone, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)


# =========================================================
# USER MODEL
# =========================================================
class User(AbstractBaseUser, PermissionsMixin):
    # BASIC
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        }
    )

    email = models.EmailField(
        _("email address"),
        max_length=255,
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        }
    )

    phone = models.CharField(
        _("phone number"),
        max_length=13,
        unique=True,
        validators=[phone_validator],
        error_messages={
            "unique": _("A user with that phone number already exists."),
        }
    )

    image = models.ImageField(
        _("profile image"),
        upload_to="users/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"])]
    )

    # ADDRESS
    country = models.CharField(_("country"), max_length=100, blank=True, null=True, default="Bangladesh")
    city = models.CharField(_("city"), max_length=100, blank=True, null=True)
    home_city = models.CharField(_("home city"), max_length=100, blank=True, null=True)
    zip_code = models.CharField(_("zip code"), max_length=20, blank=True, null=True)
    address = models.TextField(_("address"), blank=True, null=True)

    # STATUS
    is_active = models.BooleanField(_("active"), default=False, db_index=True)
    is_staff = models.BooleanField(_("staff"), default=False, db_index=True)
    is_verified = models.BooleanField(_("verified"), default=False, db_index=True)

    # TOKENS
    email_verification_token = models.UUIDField(_("email verification token"), null=True, blank=True, db_index=True)
    email_token_created_at = models.DateTimeField(_("email token created at"), null=True, blank=True)

    password_reset_token = models.UUIDField(_("password reset token"), null=True, blank=True, db_index=True)
    password_reset_token_created_at = models.DateTimeField(_("password reset token created at"), null=True, blank=True)

    # new: session token (for API authentication) alternative to JWT
    session_token = models.UUIDField(_("session token"), null=True, blank=True, db_index=True)
    session_token_created_at = models.DateTimeField(_("session token created at"), null=True, blank=True)

    # ONLINE
    last_seen = models.DateTimeField(_("last seen"), null=True, blank=True, db_index=True)

    # SECURITY
    failed_login_attempts = models.PositiveIntegerField(_("failed login attempts"), default=0)
    last_failed_login = models.DateTimeField(_("last failed login"), null=True, blank=True)
    account_locked_until = models.DateTimeField(_("account locked until"), null=True, blank=True, db_index=True)

    # new: when password changes (for old token revocation)
    password_changed_at = models.DateTimeField(_("password changed at"), null=True, blank=True)

    # TIMESTAMPS
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone"]

    class Meta:
        db_table = "account_users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-id"]

        indexes = [
            models.Index(fields=["email_verification_token"]),
            models.Index(fields=["password_reset_token"]),
            models.Index(fields=["session_token"]),
            models.Index(fields=["is_active", "is_verified"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["last_seen"]),
            models.Index(fields=["account_locked_until"]),
        ]

    # =====================================================
    # CLEAN (validation only)
    # =====================================================
    def clean(self):
        super().clean()

        if self.phone:
            if not normalize_phone_number(self.phone):
                raise ValidationError({"phone": _("Invalid phone number")})

        if self.email:
            from django.core.validators import validate_email
            try:
                validate_email(self.email)
            except ValidationError:
                raise ValidationError({"email": _("Invalid email format")})

    # =====================================================
    # SAVE (normalization only)
    # =====================================================
    def save(self, *args, **kwargs):
        if self.username:
            self.username = self.username.strip().lower()

        if self.email:
            self.email = self.email.strip().lower()

        if self.phone:
            self.phone = normalize_phone_number(self.phone)

        super().save(*args, **kwargs)

    # =====================================================
    # ONLINE STATUS
    # =====================================================
    @property
    def is_online(self):
        if not self.last_seen:
            return False
        
        return bool(
            self.last_seen and
            timezone.now() <= self.last_seen + timedelta(seconds=ONLINE_TIMEOUT_SECONDS)
        )

    def refresh_last_seen(self):
        now = timezone.now()

        if not self.last_seen or (now - self.last_seen).total_seconds() > LAST_SEEN_UPDATE_INTERVAL:
            self.last_seen = now
            self.save(update_fields=["last_seen"])

    # =====================================================
    # ACCOUNT LOCK
    # =====================================================
    @property
    def is_locked(self):
        if not self.account_locked_until:
            return False
        
        if timezone.now() >= self.account_locked_until:
            # Auto unlock
            self.unlock_account_if_expired()
            return False
        
        return True

    def get_lock_remaining_time(self):
        """Remaining lock time in minutes"""
        if not self.account_locked_until:
            return 0
        
        remaining = self.account_locked_until - timezone.now()
        if remaining.total_seconds() <= 0:
            return 0
        
        return int(remaining.total_seconds() / 60)

    # =====================================================
    # FAILED LOGIN
    # =====================================================
    def record_failed_login_attempt(self):
        now = timezone.now()

        with transaction.atomic():
            user = User.objects.select_for_update().get(pk=self.pk)

            user.failed_login_attempts += 1
            user.last_failed_login = now

            if user.failed_login_attempts >= MAX_FAILED_ATTEMPTS:
                user.account_locked_until = now + timedelta(minutes=ACCOUNT_LOCK_MINUTES)
                logger.warning(f"User {user.username} account locked due to {MAX_FAILED_ATTEMPTS} failed attempts")

            user.save(update_fields=[
                "failed_login_attempts",
                "last_failed_login",
                "account_locked_until"
            ])

    def reset_login_attempts(self):
        with transaction.atomic():
            user = User.objects.select_for_update().get(pk=self.pk)

            user.failed_login_attempts = 0
            user.last_failed_login = None
            user.account_locked_until = None

            user.save(update_fields=[
                "failed_login_attempts",
                "last_failed_login",
                "account_locked_until"
            ])

    def unlock_account_if_expired(self):
        if self.account_locked_until and timezone.now() >= self.account_locked_until:
            self.account_locked_until = None
            self.failed_login_attempts = 0
            self.save(update_fields=[
                "account_locked_until",
                "failed_login_attempts"
            ])
            logger.info(f"User {self.username} account unlocked automatically")

    # =====================================================
    # EMAIL TOKEN
    # =====================================================
    def generate_email_verification_token(self):
        # Revoke old token
        self.email_verification_token = None
        self.email_token_created_at = None
        self.save(update_fields=["email_verification_token", "email_token_created_at"])
        
        # Generate new token
        self.email_verification_token = uuid.uuid4()
        self.email_token_created_at = timezone.now()

        self.save(update_fields=["email_verification_token", "email_token_created_at"])
        logger.info(f"Email verification token generated for user {self.username}")

    def has_valid_email_verification_token(self):
        if not self.email_verification_token or not self.email_token_created_at:
            return False
        
        if timezone.now() > self.email_token_created_at + timedelta(hours=EMAIL_TOKEN_EXPIRE_HOURS):
            logger.warning(f"Email verification token expired for user {self.username}")
            return False
        
        return True

    def mark_email_as_verified(self):
        self.is_verified = True
        self.is_active = True
        self.email_verification_token = None
        self.email_token_created_at = None

        self.save(update_fields=[
            "is_verified",
            "is_active",
            "email_verification_token",
            "email_token_created_at"
        ])
        logger.info(f"User {self.username} email verified")

    # =====================================================
    # PASSWORD RESET
    # =====================================================
    def generate_password_reset_token(self):
        # Revoke old token
        self.password_reset_token = None
        self.password_reset_token_created_at = None
        self.save(update_fields=["password_reset_token", "password_reset_token_created_at"])

        self.password_reset_token = uuid.uuid4()
        self.password_reset_token_created_at = timezone.now()

        self.save(update_fields=[
            "password_reset_token",
            "password_reset_token_created_at"
        ])
        logger.info(f"Password reset token generated for user {self.username}")

    def has_valid_password_reset_token(self):
        if not self.password_reset_token or not self.password_reset_token_created_at:
            return False

        if timezone.now() > self.password_reset_token_created_at + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS):
            logger.warning(f"Password reset token expired for user {self.username}")
            return False

        return True

    def remove_password_reset_token(self):
        self.password_reset_token = None
        self.password_reset_token_created_at = None

        self.save(update_fields=[
            "password_reset_token",
            "password_reset_token_created_at"
        ])

    # =====================================================
    # SESSION TOKEN
    # =====================================================
    def generate_session_token(self):
        """Generate session token for API authentication"""
        self.session_token = uuid.uuid4()
        self.session_token_created_at = timezone.now()

        self.save(update_fields=[
            "session_token",
            "session_token_created_at"
        ])
        logger.info(f"Session token generated for user {self.username}")
        return self.session_token

    def has_valid_session_token(self):
        """Check if session token is valid (for API useCase)"""
        if not self.session_token or not self.session_token_created_at:
            return False
        
        # Session expires in 7 days (optional)
        return timezone.now() <= self.session_token_created_at + timedelta(days=7)

    def revoke_session_token(self):
        """Revoke session token (for logout)"""
        self.session_token = None
        self.session_token_created_at = None

        self.save(update_fields=[
            "session_token",
            "session_token_created_at"
        ])
        logger.info(f"Session token revoked for user {self.username}")

    # =====================================================
    # PASSWORD MANAGEMENT
    # =====================================================
    def set_password(self, raw_password):
        """Set password with validation"""
        if raw_password:
            validate_password_strength(raw_password)
        
        super().set_password(raw_password)
        self.password_changed_at = timezone.now()
        
        # Revoke old tokens (security)
        self.remove_password_reset_token()
        self.revoke_session_token()

    def reset_password(self, new_password, token=None):
        """Reset password (with token validation)"""
        if token and not self.has_valid_password_reset_token():
            raise ValidationError(_("Invalid or expired password reset token"))
        
        self.set_password(new_password)
        self.remove_password_reset_token()
        self.reset_login_attempts()
        self.save()
        
        logger.info(f"User {self.username} password reset successfully")

    # =====================================================
    # DISPLAY
    # =====================================================
    def get_last_seen_display(self):
        if self.is_online:
            return "Online"
        if not self.last_seen:
            return "Never"
        return localtime(self.last_seen).strftime("%Y-%m-%d %H:%M")

    def get_full_address(self):
        """Get full address string"""
        parts = []
        if self.address:
            parts.append(self.address)
        if self.city:
            parts.append(self.city)
        if self.zip_code:
            parts.append(self.zip_code)
        if self.country:
            parts.append(self.country)
        return ", ".join(parts)

    def natural_key(self):
        return (self.username,)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.username} (ID: {self.pk})>"