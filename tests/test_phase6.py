# test_phase6.py

from pathlib import Path
import shutil

from core import EncFileManager
from encryptors import CaesarEncryptor, XOREncryptor
from FernetEncryptor import FernetEncryptor


TEST_VAULT = Path("phase6_test_vault")


def readiness_test():
    print("\n--- Starting Phase 6 Readiness Test ---")

    if TEST_VAULT.exists():
        shutil.rmtree(TEST_VAULT)

    try:
        encryptors = [
            (
                "Caesar",
                CaesarEncryptor(key=5),
                "Hello Caesar Cipher!"
            ),
            (
                "XOR",
                XOREncryptor(key=123),
                "Hello XOR Cipher!"
            ),
            (
                "Fernet",
                FernetEncryptor(
                    key_path=TEST_VAULT / "test_secret.key"
                ),
                "Hello Fernet Encryption!"
            ),
        ]

        for name, encryptor, content in encryptors:
            print(f"\nTesting {name}Encryptor...")

            manager = EncFileManager(
                vault_folder=TEST_VAULT,
                encryptor=encryptor
            )

            filename = f"file_{name.lower()}.txt"

            # 1. Add file
            assert manager.add_file(filename, content), \
                f"{name}: failed to write file"

            print(f"  [OK] {filename} written successfully")

            # 2. Verify file exists
            assert filename in manager, \
                f"{name}: file was not found in vault"

            print(f"  [OK] {filename} exists in vault")

            # 3. Read and decrypt file
            read_content = manager.read_file(filename)

            assert read_content == content, \
                f"{name}: decrypted content does not match original"

            print(f"  [OK] {filename} read successfully")

            # 4. Verify file is listed
            assert filename in manager.list_files(), \
                f"{name}: file missing from file list"

            print(f"  [OK] {filename} appears in file list")

            # 5. Delete file
            assert manager.delete_file(filename), \
                f"{name}: failed to delete file"

            print(f"  [OK] {filename} deleted successfully")

            # 6. Confirm deletion
            assert filename not in manager, \
                f"{name}: file still exists after deletion"

        print("\nPhase 6 readiness test passed successfully ✔")

    finally:
        # Remove all test artifacts
        if TEST_VAULT.exists():
            shutil.rmtree(TEST_VAULT)


if __name__ == "__main__":
    readiness_test()
