from pathlib import Path

class CaesarEncryptor:
    """
    Simple Caesar Cipher for text-based encryption.
     Not secure, for educational use only.
    """
    def __init__(self, key=3):
        self._key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key

    @staticmethod
    def caesar_encrypt(text, key):
        return ''.join(chr((ord(c) + key) % 256 ) for c in text)

    @staticmethod
    def caesar_decrypt(text, key):
        return ''.join(chr((ord(c) - key) % 256) for c in text)








