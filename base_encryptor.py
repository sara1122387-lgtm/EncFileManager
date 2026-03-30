#base_encryptor.py
from abc import ABC,abstractmethod

class BaseEncryptor(ABC):
    name: str #حتى نُجبر كل Encryptor أن يكون له اسم.

    @abstractmethod
    def encrypt(self, data: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, data: bytes) -> bytes:
        pass