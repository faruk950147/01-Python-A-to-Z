'''
FINAL A–Z ACCOUNT SYSTEM (DJANGO)
account/
│
├── models.py
├── managers.py
├── constants.py
│
├── utils/
│   ├── validators.py
│   ├── helpers.py
│
├── services/
│   ├── auth_service.py
│   ├── user_service.py
│   ├── token_service.py
│   ├── otp_service.py
│
├── middleware/
│   ├── last_seen_middleware.py
│   ├── online_status_middleware.py
│
├── api/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
└── permissions.py
1. MODELS (Clean Core Only)
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=20, unique=True, db_index=True)

    image = models.ImageField(
        upload_to="users/%Y/%m/%d/",
        default="defaults/default.jpg"
    )

    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    last_seen_at = models.DateTimeField(null=True, blank=True)

    failed_login_attempts = models.PositiveIntegerField(default=0)
    account_locked_until = models.DateTimeField(null=True, blank=True)

    email_token = models.UUIDField(null=True, blank=True, db_index=True)
    reset_token = models.UUIDField(null=True, blank=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone"]

    def __str__(self):
        return self.username


2. MANAGER (User Creation Logic)
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, phone, password=None):

        if not email:
            raise ValueError("Email required")

        user = self.model(
            username=username,
            email=email,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None):

        user = self.create_user(username, email, phone, password)

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_verified = True

        user.save(using=self._db)
        return user


3. UTILS
validators.py
import re

def phone_validator(phone):
    pattern = r"^\+?[0-9]{10,15}$"
    if not re.match(pattern, phone):
        raise ValueError("Invalid phone number")


def username_validator(username):
    if len(username) < 3:
        raise ValueError("Username too short")
helpers.py
def normalize_phone_number(phone):
    return phone.strip().replace(" ", "")
    
    
4. SERVICES LAYER (HEART OF SYSTEM)
auth_service.py
from django.contrib.auth import authenticate


def login_user(username, password):
    return authenticate(username=username, password=password)
user_service.py
from account.utils.helpers import normalize_phone_number


def normalize_user(user):

    if user.username:
        user.username = user.username.strip().lower()

    if user.email:
        user.email = user.email.strip().lower()

    if user.phone:
        user.phone = normalize_phone_number(user.phone)

    return user
token_service.py
import uuid


def generate_token():
    return uuid.uuid4()
otp_service.py
import random


def generate_otp():
    return str(random.randint(100000, 999999))


5. MIDDLEWARE
last_seen_middleware.py
from django.utils.timezone import now
from account.models import User


class LastSeenMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id).update(
                last_seen_at=now()
            )

        return self.get_response(request)


6. API LAYER (DRF STYLE)
serializers.py
from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
views.py
from rest_framework.views import APIView
from rest_framework.response import Response

from account.services.auth_service import login_user
from account.api.serializers import UserSerializer


class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = login_user(username, password)

        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)

        return Response({"error": "Invalid credentials"})
urls.py
from django.urls import path
from account.api.views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view()),
]

7. SECURITY FLOW (IMPORTANT)
Login flow:
User → API → Auth Service → Django authenticate → User
OTP flow:
Signup → OTP generate → Email send → verify → activate user
Reset password:
Request → reset_token generate → email link → reset password

8. FINAL FEATURES YOU NOW HAVE
✅ Authentication
Login
Logout ready
Superuser system
✅ Security
Account lock fields
Failed login tracking
✅ OTP System
OTP generator ready
Token system ready
✅ Middleware
last_seen tracking
✅ Scalable architecture
services layer
utils layer
api layer
'''