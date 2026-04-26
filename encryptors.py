#encryptors.py

from base_encryptor import BaseEncryptor

class CaesarEncryptor(BaseEncryptor):
    name = "caesar"
    """
    Simple Caesar Cipher for text-based encryption.
     Not secure, for educational use only.
    """
    def __init__(self, key: int = 3):
        self.key = key

    def encrypt(self, data: bytes) -> bytes:
        return bytes((b + self.key) % 256 for b in data)

    def decrypt(self, data: bytes) -> bytes:
        return bytes ((b - self.key) % 256 for b in data)


class XOREncryptor(BaseEncryptor):
    name = "xor"
    """
        Simple XOR encryption.
        Not secure — educational demonstration only.
        """
    def __init__(self, key: int = 42):
        self.key = key

    def encrypt(self, data: bytes) -> bytes:
        return bytes(b ^ self.key for b in data)

    def decrypt(self, data: bytes) -> bytes:
        return bytes(b ^ self.key for b in data)
