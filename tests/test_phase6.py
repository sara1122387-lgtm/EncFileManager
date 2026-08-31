# test_phase6.py

from pathlib import Path
import shutil

from core import EncFileManager
from encryptors import CaesarEncryptor, XOREncryptor
from FernetEncryptor import FernetEncryptor


TEST_VAULT = Path("phase6_test_vault")
TEST_KEY = Path("phase6_test_secret.key")


def readiness_test():
    print("\n--- Starting Phase 6 Readiness Test ---")

    # Start with a clean test environment
    if TEST_VAULT.exists():
        shutil.rmtree(TEST_VAULT)

    if TEST_KEY.exists():
        TEST_KEY.unlink()

    tests = [
        (
            "Caesar",
            CaesarEncryptor(key=5),
            "file_caesar.txt",
            "Hello Caesar Cipher!"
        ),
        (
            "XOR",
            XOREncryptor(key=123),
            "file_xor.txt",
            "Hello XOR Cipher!"
        ),
        (
            "Fernet",
            FernetEncryptor(key_path=TEST_KEY),
            "file_fernet.txt",
            "Hello Fernet Encryption!"
        )
    ]

    try:
        for name, encryptor, file_name, content in tests:

            print(f"\n--- Testing {name}Encryptor ---")

            manager = EncFileManager(
                vault_folder=TEST_VAULT,
                encryptor=encryptor
            )

            # 1. Add file
            assert manager.add_file(file_name, content), \
                f"{name}: failed to write file"

            print(f"[OK] {file_name} written successfully")

            # 2. Read file
            read_content = manager.read_file(file_name)

            assert read_content == content, \
                f"{name}: decrypted content does not match original"

            print(f"[OK] {file_name} read successfully")

            # 3. Verify file exists
            assert file_name in manager, \
                f"{name}: file missing from vault"

            print(f"[OK] {file_name} exists in vault")

            # 4. Verify vault length
            assert len(manager) == 1, \
                f"{name}: unexpected vault length"

            print("[OK] Vault length verified")

            # 5. Delete file
            assert manager.delete_file(file_name), \
                f"{name}: failed to delete file"

            print(f"[OK] {file_name} deleted successfully")

            # 6. Verify deletion
            assert file_name not in manager, \
                f"{name}: file still exists after deletion"

            print("[OK] File removal verified")

        print("\nALL PHASE 6 READINESS TESTS PASSED SUCCESSFULLY")

    finally:
        # Remove all test artifacts
        if TEST_VAULT.exists():
            shutil.rmtree(TEST_VAULT)

        if TEST_KEY.exists():
            TEST_KEY.unlink()


if __name__ == "__main__":
    readiness_test()
