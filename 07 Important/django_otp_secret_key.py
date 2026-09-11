import hashlib
import hmac
import secrets
import re

'''
If your goal is to actually use these modules, here’s a quick summary:

hashlib - Create hashes like SHA256, MD5.
hmac - Generate cryptographic message signatures.
secrets - Generate secure random numbers and tokens (good for passwords, OTPs).
re - Perform regex-based string matching and manipulation.

For example, a simple SHA256 hash:
'''
'''
# ==================================== hashlib ====================================
# Original message
message = "Hello World"

# Hash the message
hash_object = hashlib.sha256(message.encode())
hash_string = hash_object.hexdigest()
print(f"Hash: {hash_string}")

# Verify the message (if message is changed, verification will fail)
check_message = "Hello World"  # Try changing this to see verification fail
check_hash = hashlib.sha256(check_message.encode()).hexdigest()

if check_hash == hash_string:
    print("Message verified! Hash matches.")
else:
    print("Hash mismatch. Message altered!")

# ==================================== hash message authentication code ====================================
original_message = "Hello World"
key = b"my_secret_key"  # Must be bytes

# Generate HMAC
# new is a constructor that creates a new HMAC object
h = hmac.new(key, original_message.encode(), hashlib.sha256) 

# Verify HMAC
check_h = hmac.new(key, original_message.encode(), hashlib.sha256) 
if check_h.hexdigest() == h.hexdigest():
    print("HMAC verified!")
else:
    print("HMAC mismatch!")
'''

# ==================================== secrets ====================================
# Generate a secure random token
# token = secrets.token_hex(16)
# print(f"Secure token: {token}")

# Generate a secure random integer
random_int = secrets.randbelow(100)
print(f"Random integer: {random_int}") # 0-99 of random amount

# Generate a secure random choice
# choices = ['apple', 'banana', 'cherry']
# random_choice = secrets.choice(choices)
# print(f"Random choice: {random_choice}")

