import os
import hashlib
import hmac
import secrets
from ecdsa import SigningKey, SECP256k1

# Generate secure random private key
def generate_private_key():
    return secrets.token_bytes(32)

# Derive public key from private key
def private_to_public(private_key):
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    return sk.verifying_key.to_string()

# Create a wallet address from public key
def public_to_address(public_key):
    sha256 = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new("ripemd160", sha256).digest()
    return ripemd160.hex()

# Sign message using private key
def sign_message(private_key, message):
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    return sk.sign(message.encode()).hex()

# Verify signed message
def verify_signature(public_key, message, signature):
    from ecdsa import VerifyingKey
    vk = VerifyingKey.from_string(public_key, curve=SECP256k1)
    return vk.verify(bytes.fromhex(signature), message.encode())
