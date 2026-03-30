from base_encryptor import BaseEncryptor

class EncryptionRegistry:
    def __init__(self):
        self.encryptors: list[BaseEncryptor] = []

    def register(self, encryptor: BaseEncryptor):
        self.encryptors.append(encryptor)

    def get_encryptor(self, name: str) -> BaseEncryptor | None:
        name = name.lower()
        return next(
            filter(lambda e: e.name.lower() == name, self.encryptors),
            None
        )
