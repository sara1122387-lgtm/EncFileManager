from core import EncFileManager
from FernetEncryptor import FernetEncryptor
import os

def test_phase_5():
    print("\n--- Starting Phase 5 Test ---")

    # 1. إنشاء الإنكربتور
    encryptor = FernetEncryptor(key_path="secret.key")
    print("[OK] FernetEncryptor initialized")

    # 2. إنشاء مدير الملفات
    manager = EncFileManager(vault_folder="vault_test", encryptor=encryptor)
    print("[OK] EncFileManager created")

    # 3. حذف الملفات القديمة داخل vault_test (تنظيف)
    for f in manager.list_files():
        manager.delete_file(f)
    print("[OK] Vault cleaned")

    # 4. محاولة إضافة ملف مشفر
    filename = "test_secure.txt"
    content = "This is a secret message for phase 5!"

    added = manager.add_file(filename, content)
    assert added, "❌ Failed to add encrypted file"

    print("[OK] Encrypted file created")

    # 5. تأكد أن الملف مخزن مشفرًا وليس نصًا واضحًا
    raw_path = os.path.join("vault_test", filename)
    with open(raw_path, "rb") as f:
        raw = f.read()

    assert content.encode("utf-8") not in raw, "❌ File is NOT encrypted!"
    print("[OK] File is stored encrypted (not plain text)")

    # 6. قراءة الملف بعد فك التشفير
    decrypted = manager.read_file(filename)
    assert decrypted == content, "❌ Decryption failed — content mismatch"

    print("[OK] Decryption successful")

    # 7. حذف الملف
    deleted = manager.delete_file(filename)
    assert deleted, "❌ Failed to delete file"

    print("[OK] File deletion successful")

    print("\n🎉 ALL PHASE 5 TESTS PASSED SUCCESSFULLY 🎉")


if __name__ == "__main__":
    test_phase_5()
