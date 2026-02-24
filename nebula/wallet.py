from .crypto import generate_private_key, private_to_public, public_to_address

class Wallet:
    def __init__(self):
        # Generate new wallet on initialization
        self.private_key = generate_private_key()
        self.public_key = private_to_public(self.private_key)
        self.address = public_to_address(self.public_key)

    def get_address(self):
        return self.address

    def export_private_key(self):
        # WARNING: Never expose private keys in production systems
        return self.private_key.hex()
