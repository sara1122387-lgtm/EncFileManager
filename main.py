#الفقرة الأولى\مراجعة وتحقق
# from encryption_registry import EncryptionRegistry
# from encryptors import CaesarEncryptor, XOREncryptor
# from FernetEncryptor import FernetEncryptor
#
# # إنشاء registry
# registry = EncryptionRegistry()
#
# # تسجيل جميع الاستراتيجيات
# registry.register(CaesarEncryptor())
# registry.register(XOREncryptor())
# registry.register(FernetEncryptor())
#
# # البيانات التجريبية
# original_data = b"Hello OOP2"
#
# print("=== Running Full Encryption Test ===\n")
#
# for encryptor in registry.encryptors:
#     print(f"Testing: {encryptor.name}")
#
#     encrypted = encryptor.encrypt(original_data)
#     decrypted = encryptor.decrypt(encrypted)
#
#     if decrypted == original_data:
#         print("✔ Success\n")
#     else:
#         print("✘ Failed\n")



#الفقرة الثانية\ Pointer
# from encryption_registry import EncryptionRegistry
# from encryptors import CaesarEncryptor, XOREncryptor
# from FernetEncryptor import FernetEncryptor
# from core import EncFileManager

# registry = EncryptionRegistry()
#
# registry.register(CaesarEncryptor())
# registry.register(XOREncryptor())
# registry.register(FernetEncryptor())

# نفس الكائن
# shared_encryptor = registry.get_encryptor("xor")
#
# manager1 = EncFileManager(encryptor=shared_encryptor)
# manager2 = EncFileManager(encryptor=shared_encryptor)
#
# print("Same object?", manager1.encryptor is manager2.encryptor)
#
# # تعديل داخلي (تجربة)
# shared_encryptor.key = 99
#
# print("Manager1 key:", manager1.encryptor.key)
# print("Manager2 key:", manager2.encryptor.key)


#الفقرة الثالثة\ Friend Function
# from utils import inspect_file
#
# manager1.add_file("test.txt", "hello")
#
# handler = manager1._get_handler("test.txt")
#
# info = inspect_file(handler)
#
# print(info)



#الفقرة الرابعة\ Advanced Operator Overloading

from core import EncFileManager

manager1 = EncFileManager(vault_folder="vault1")
manager2 = EncFileManager(vault_folder="vault2")

manager1.add_file("a.txt", "Hello")
manager2.add_file("b.txt", "World")
manager2.add_file("c.txt", "World")

print(manager1)          # __str__
print(manager2)

print(manager1 < manager2)  # __lt__
print(manager1 > manager2)  # __gt__

merg = manager1 + manager2  # __add__

print(merg)
