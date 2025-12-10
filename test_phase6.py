from core import EncFileManager
from encryptors import CaesarEncryptor
from encryptors import XOREncryptor
from  FernetEncryptor import FernetEncryptor
from pathlib import Path

def readiness_test():
    print("Starting readiness test for Phase 6...")

    vault = Path("vault")
    vault.mkdir(exist_ok=True)

    test_files = {
        "file_caesar.txt": "Hello Caesar Cipher!",
        "file_xor.txt": "Hello XOR Cipher!",
        "file_fernet.txt": "Hello Fernet Encryption!"
    }

    encryptors = {
        "Caesar": CaesarEncryptor(key=5),
        "XOR": XOREncryptor(key=123),
        "Fernet": FernetEncryptor(key_path="secret.key")
    }

    for name, encryptor in encryptors.items():
        print(f"\nTesting {name}Encryptor...")
        manager = EncFileManager(vault_folder=vault, encryptor=encryptor)

        # اختيار الملف النصي الخاص بهذا التشفير
        file_name, content = list(test_files.items())[list(encryptors.keys()).index(name)]

        # 1. إضافة الملف
        if manager.add_file(file_name, content):
            print(f"✅ {file_name} written successfully.")
        else:
            print(f"❌ Failed to write {file_name}.")

        # 2. قراءة الملف
        read_content = manager.read_file(file_name)
        if read_content == content:
            print(f"✅ {file_name} read successfully and matches original.")
        else:
            print(f"❌ Read content does not match original!")
            print("Expected:", content)
            print("Got:", read_content)

        # 3. التحقق من قائمة الملفات
        if file_name in manager.list_files():
            print(f"✅ {file_name} exists in vault.")
        else:
            print(f"❌ {file_name} missing in vault!")

        # 4. حذف الملف بعد الاختبار
        if manager.delete_file(file_name):
            print(f"✅ {file_name} deleted successfully.")
        else:
            print(f"❌ Failed to delete {file_name}.")

    print("\nReadiness test completed.")

if __name__ == "__main__":
    readiness_test()
