""" create_key_pair.py """

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate a new private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Get the public key from the private key
public_key = private_key.public_key()

# Serialize the private key to PEM format
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()  # For demonstration; consider using a password in production
)

# Serialize the public key to PEM format
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write the keys to files
with open("/tmp/private_key.pem", "wb") as f:
    f.write(pem_private)

with open("/tmp/public_key.pem", "wb") as f:
    f.write(pem_public)

print("Private and public keys generated and saved!")
