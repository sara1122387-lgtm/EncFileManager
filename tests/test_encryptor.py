# test_encryptor.py

from base_encryptor import BaseEncryptor
from encryptors import CaesarEncryptor, XOREncryptor
from FernetEncryptor import FernetEncryptor
from pipeline import EncryptionPipeline


def test_encryptor(encryptor: BaseEncryptor, label: str):
    original_data = b"Hello EncFileManager!"

    encrypted = encryptor.encrypt(original_data)
    decrypted = encryptor.decrypt(encrypted)

    assert encrypted != original_data, f"{label}: encryption produced unchanged data"
    assert decrypted == original_data, f"{label}: decryption failed"

    print(f"{label}: passed")


def main():
    encryptors = [
        (CaesarEncryptor(key=3), "Caesar"),
        (XOREncryptor(key=42), "XOR"),
        (FernetEncryptor(), "Fernet"),
    ]

    for encryptor, label in encryptors:
        test_encryptor(encryptor, label)

    # Test encryption pipeline
    pipeline = (
        CaesarEncryptor(key=3)
        | XOREncryptor(key=42)
        | FernetEncryptor()
    )

    test_encryptor(pipeline, "Pipeline")

    print("\nAll encryption tests passed successfully.")


if __name__ == "__main__":
    main()
