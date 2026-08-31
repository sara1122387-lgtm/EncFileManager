from core import EncFileManager
from encryptors import CaesarEncryptor, XOREncryptor
from FernetEncryptor import FernetEncryptor


def run_test(encryptor, label):
    print(f"\n--- Testing {label} ---")

    manager = EncFileManager(vault_folder="test_vault", encryptor=encryptor)

    # 1. Add file
    assert manager.add_file("test.txt", "Hello World") == True

    # 2. Check existence
    assert "test.txt" in manager

    # 3. Check length
    assert len(manager) >= 1

    # 4. Read file
    content = manager.read_file("test.txt")
    assert content == "Hello World"

    # 5. Delete file
    assert manager.delete_file("test.txt") == True

    # 6. Confirm deletion
    assert "test.txt" not in manager

    print(f"{label} passed ✔")


if __name__ == "__main__":
    run_test(None, "No Encryption")
    run_test(CaesarEncryptor(3), "Caesar")
    run_test(XOREncryptor(42), "XOR")
    run_test(FernetEncryptor(), "Fernet")

    print("\nAll tests passed successfully ✔")