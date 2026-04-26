from base_encryptor import BaseEncryptor

class EncryptionPipeline(BaseEncryptor):
    name = 'pipeline'

    def __init__(self, encryptors):
        self.encryptors = encryptors

    def encrypt(self, data: bytes) -> bytes:
        for enc in self.encryptors:
            data = enc.encrypt(data)
        return data

    def decrypt(self, data: bytes) -> bytes:
        for enc in reversed(self.encryptors):
            data = enc.decrypt(data)
        return data

# pipe باستخدام |
    def __or__(self, other):
        from base_encryptor import BaseEncryptor

        if isinstance(other, BaseEncryptor):
            return EncryptionPipeline(self.encryptors + [other])
        return NotImplemented

    def __ror__(self, other):
        from base_encryptor import BaseEncryptor

        if isinstance(other, BaseEncryptor):
            return EncryptionPipeline([other] + self.encryptors)
        return NotImplemented

    def __repr__(self):
        names = " -> ".join(e.name for e in self.encryptors)
        return f"<Pipeline: {names}>"