# test_phase5.py

from pathlib import Path
import shutil

from core import EncFileManager
from FernetEncryptor import FernetEncryptor


TEST_VAULT = Path("vault_test")
TEST_KEY = Path("test_secret.key")


def test_phase_5():
    print("\n--- Starting Phase 5 Test ---")

    # Start with a clean test environment
    if TEST_VAULT.exists():
        shutil.rmtree(TEST_VAULT)

    if TEST_KEY.exists():
        TEST_KEY.unlink()

    try:
        # 1. Create Fernet encryptor
        encryptor = FernetEncryptor(key_path=TEST_KEY)
        print("[OK] FernetEncryptor initialized")

        # 2. Create file manager
        manager = EncFileManager(
            vault_folder=TEST_VAULT,
            encryptor=encryptor
        )
        print("[OK] EncFileManager created")

        # 3. Add encrypted file
        filename = "test_secure.txt"
        content = "This is a secret message for phase 5!"

        added = manager.add_file(filename, content)
        assert added, "Failed to add encrypted file"

        print("[OK] Encrypted file created")

        # 4. Verify that plaintext is not stored directly
        raw_path = TEST_VAULT / filename

        with open(raw_path, "rb") as f:
            raw = f.read()

        assert content.encode("utf-8") not in raw, \
            "File is NOT encrypted!"

        print("[OK] File is stored encrypted (not plain text)")

        # 5. Read the file and verify decryption
        decrypted = manager.read_file(filename)

        assert decrypted == content, \
            "Decryption failed — content mismatch"

        print("[OK] Decryption successful")

        # 6. Delete the file
        deleted = manager.delete_file(filename)

        assert deleted, \
            "Failed to delete file"

        print("[OK] File deletion successful")

        # 7. Verify deletion
        assert filename not in manager, \
            "File still exists after deletion"

        print("[OK] File removal verified")

        print("\nALL PHASE 5 TESTS PASSED SUCCESSFULLY")

    finally:
        # Remove all test artifacts
        if TEST_VAULT.exists():
            shutil.rmtree(TEST_VAULT)

        if TEST_KEY.exists():
            TEST_KEY.unlink()


if __name__ == "__main__":
    test_phase_5()
