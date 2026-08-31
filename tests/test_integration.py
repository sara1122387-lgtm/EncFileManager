# test_integration.py

from pathlib import Path
import shutil

from core import EncFileManager
from encryptors import CaesarEncryptor, XOREncryptor
from FernetEncryptor import FernetEncryptor


TEST_VAULT = Path("test_vault")


def run_test(encryptor_factory, label):
    print(f"\n--- Testing {label} ---")

    # Start with a clean test environment
    if TEST_VAULT.exists():
        shutil.rmtree(TEST_VAULT)

    encryptor = encryptor_factory()

    manager = EncFileManager(
        vault_folder=TEST_VAULT,
        encryptor=encryptor
    )

    try:
        # 1. Add file
        assert manager.add_file("test.txt", "Hello World"), \
            f"{label}: failed to add file"

        # 2. Check file existence
        assert "test.txt" in manager, \
            f"{label}: file was not found after creation"

        # 3. Check vault length
        assert len(manager) == 1, \
            f"{label}: unexpected vault length"

        # 4. Read file and verify content
        content = manager.read_file("test.txt")

        assert content == "Hello World", \
            f"{label}: decrypted content does not match original content"

        # 5. Delete file
        assert manager.delete_file("test.txt"), \
            f"{label}: failed to delete file"

        # 6. Confirm deletion
        assert "test.txt" not in manager, \
            f"{label}: file still exists after deletion"

        print(f"{label} passed ✔")

    finally:
        # Remove all test artifacts, including the test key
        if TEST_VAULT.exists():
            shutil.rmtree(TEST_VAULT)


def main():
    tests = [
        (lambda: None, "No Encryption"),
        (lambda: CaesarEncryptor(key=3), "Caesar"),
        (lambda: XOREncryptor(key=42), "XOR"),
        (
            lambda: FernetEncryptor(
                key_path=TEST_VAULT / "test_secret.key"
            ),
            "Fernet"
        ),
    ]

    for encryptor_factory, label in tests:
        run_test(encryptor_factory, label)

    print("\nAll integration tests passed successfully ✔")


if __name__ == "__main__":
    main()
