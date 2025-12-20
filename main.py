from core import FileHandler, EncFileManager
from encryptors import CaesarEncryptor

# # ==========================
# # اختبار FileHandler
# # ==========================
#
# # التحقق من دالة is_valid_extension
# print(FileHandler.is_valid_extension('file.txt'))      # True
# print(FileHandler.is_valid_extension('document'))      # False
#
# # إنشاء كائن FileHandler (Path يتحول داخل __init__)
# file = FileHandler("vault/test.txt")
#
# # كتابة نص
# file.write("Hello world!")
#
# # قراءة النص
# print("Content:", file.read())
#
# # تغيير الاسم إلى اسم جديد
# try:
#     file.rename("vault/hello.txt")
# except FileExistsError:
#     print("Cannot rename: target file already exists")
#
# # قراءة النص بعد التغيير
# print("Content after rename:", file.read())
#
# # حذف الملف
# file.delete()
#
# # ==========================
# # اختبار EncFileManager
# # ==========================
# vault = EncFileManager()
#
# # إضافة ملفات
# vault.add_file("test1.txt", "Hello Vault!")
# vault.add_file("test2.txt", "Second file content")
#
# # عرض الملفات
# print("Files in vault:", vault.list_files())
#
# # قراءة محتوى ملف
# print("Content of test1.txt:", vault.read_file("test1.txt"))
#
# # حذف ملف
# vault.delete_file("test1.txt")
# print("Files after deletion:", vault.list_files())
#
# # عدد الملفات
# print("Number of files in vault:", vault.file_count)
#
# # ==========================
# # اختبار إضافة ملفات صحيحة وخاطئة
# # ==========================
# # إضافة ملف صحيح الامتداد
# vault.add_file("test.txt", "Hello world!")
#
# # محاولة إضافة ملف خاطئ الامتداد
# vault.add_file("badfile.exe", "Should not work")
#
# # قراءة الملف
# content = vault.read_file("test.txt")
# print("Content read:", content)
#
# # حذف الملف
# vault.delete_file("test.txt")
#
# # محاولة قراءة بعد الحذف لتأكيد أن الملف اختفى
# content_after_delete = vault.read_file("test.txt")
# print("Content after delete:", content_after_delete)


# encryptor = CaesarEncryptor(key=3)
# file = EncryptedFileHandler("vault/test_encrypted.txt", encryptor)
# file.write_encrypted("Hello Phase4!")
# encrypted = file.read()           # هذا نص مشفر
# decrypted = file.read_decrypted() # هذا النص الأصلي
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)

# encryptor = CaesarEncryptor(key=5)
# vault = EncFileManager(encryptor=encryptor)
#
# # إضافة ملف مشفر
# vault.add_file("secret.txt", "This is Phase4!")
#
# # قراءة الملف مفكوك التشفير
# content = vault.read_file("secret.txt")
# print("Decrypted content:", content)


# encryptor = CaesarEncryptor(key=4)
# vault = EncFileManager(encryptor=encryptor)
#
# vault.add_file("file1.txt", "Hello Phase4!")
# vault.add_file("file2.txt", "Encrypted Vault test")
#
# for f in vault.list_files():
#     content = vault.read_file(f)
#     print(f"{f}: {content}")
#
# vault.delete_file("file1.txt")
# print("After deletion:", vault.list_files())

# from FernetEncryptor import FernetEncryptor
# manager = EncFileManager(encryptor=FernetEncryptor())
#
# manager.add_file("note.txt", "Hello secure world!")
# print(manager.read_file("note.txt"))

from core import FileHandler, EncFileManager
from FernetEncryptor import FernetEncryptor
import os
import shutil

# إعداد بيئة اختبار مؤقتة
TEST_VAULT = "test_vault"
if os.path.exists(TEST_VAULT):
    shutil.rmtree(TEST_VAULT)

# تهيئة Encryptor و Manager
encryptor = FernetEncryptor(key_path='test_secret.key')
manager = EncFileManager(vault_folder=TEST_VAULT, encryptor=encryptor)

# 1. إضافة ملفات باستخدام __setitem__
manager["file1.txt"] = "Hello World!"
manager["file2.txt"] = "Python is fun"
manager["file3.txt"] = "Encrypted content"

# 2. قراءة الملفات باستخدام __getitem__
print(manager["file1.txt"])  # يجب طباعة: Hello World!
print(manager["file2.txt"])  # يجب طباعة: Python is fun

# 3. التحقق من __contains__
print("file1.txt" in manager)  # True
print("not_exist.txt" in manager)  # False

# 4. التحقق من __len__
print(len(manager))  # 3

# 5. طباعة __str__ و __repr__
print(manager)  # EncFileManager with 3 files in '...'
file_handler = FileHandler(os.path.join(TEST_VAULT, "file1.txt"))
print(str(file_handler))
print(repr(file_handler))

# 6. اختبار المقارنات __eq__ و __lt__
file_a = FileHandler(os.path.join(TEST_VAULT, "file1.txt"))
file_b = FileHandler(os.path.join(TEST_VAULT, "file2.txt"))
file_c = FileHandler(os.path.join(TEST_VAULT, "file1.txt"))

print(file_a == file_b)  # False
print(file_a == file_c)  # True
print(file_a < file_b)   # True إذا كان اسم file1 < file2

# 7. اختبار حذف الملفات
manager.delete_file("file1.txt")
manager.delete_file("file2.txt")
manager.delete_file("file3.txt")
print(len(manager))  # 0

# تنظيف الملفات المؤقتة
if os.path.exists("test_secret.key"):
    os.remove("test_secret.key")
if os.path.exists(TEST_VAULT):
    shutil.rmtree(TEST_VAULT)

print("✅ جميع Special Methods تم اختبارها بنجاح")


