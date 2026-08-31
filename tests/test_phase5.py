# test_phase5.py

from pathlib import Path
import shutil

from core import EncFileManager
from FernetEncryptor import FernetEncryptor


TEST_VAULT = Path("vault_test")
TEST_KEY = TEST_VAULT / "test_secret.key"


def test_phase_5():
    print("\n--- Starting Phase 5 Test ---")

    # Start with a clean test environment
    if TEST_VAULT.exists():
        shutil.rmtree(TEST_VAULT)

    try:
        # 1. Initialize FernetEncryptor
        encryptor = FernetEncryptor(key_path=TEST_KEY)
        print("[OK] FernetEncryptor initialized")

        # 2. Create encrypted file manager
        manager = EncFileManager(
            vault_folder=TEST_VAULT,
            encryptor=encryptor
        )
        print("[OK] EncFileManager created")

        # 3. Add encrypted file
        filename = "test_secure.txt"
        content = "This is a secret message for phase 5!"

        assert manager.add_file(filename, content), \
            "Failed to add encrypted file"

        print("[OK] Encrypted file created")

        # 4. Verify that plaintext is not stored
        raw_path = TEST_VAULT / filename

        with open(raw_path, "rb") as file:
            raw_data = file.read()

        assert content.encode("utf-8") not in raw_data, \
            "File is stored as plain text"

        print("[OK] File is stored encrypted")

        # 5. Read and decrypt the file
        decrypted = manager.read_file(filename)

        assert decrypted == content, \
            "Decryption failed: content mismatch"

        print("[OK] Decryption successful")

        # 6. Delete the file
        assert manager.delete_file(filename), \
            "Failed to delete encrypted file"

        print("[OK] File deletion successful")

        print("\nPhase 5 test passed successfully ✔")

    finally:
        # Remove all test artifacts, including the temporary key
        if TEST_VAULT.exists():
            shutil.rmtree(TEST_VAULT)


if __name__ == "__main__":
    test_phase_5()
