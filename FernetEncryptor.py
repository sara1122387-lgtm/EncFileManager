#FernetEncryptor.py

from base_encryptor import BaseEncryptor
from cryptography.fernet import Fernet
from pathlib import Path

class FernetEncryptor(BaseEncryptor):
    name = "fernet"
    def __init__(self,key_path= 'secret.key'):
        self.key_path = Path(key_path)
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)

    def _load_or_generate_key(self):
        if self.key_path.exists():
            with open(self.key_path, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as f:
                f.write(key)
            return key

    def encrypt(self, data: bytes) -> bytes:
        return self.cipher.encrypt(data)

    def decrypt(self, data: bytes) -> bytes:
        return self.cipher.decrypt(data)
