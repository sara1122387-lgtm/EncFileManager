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
from encryption_registry import EncryptionRegistry
from encryptors import CaesarEncryptor, XOREncryptor
from FernetEncryptor import FernetEncryptor
from core import EncFileManager

registry = EncryptionRegistry()

registry.register(CaesarEncryptor())
registry.register(XOREncryptor())
registry.register(FernetEncryptor())

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
from encryption_registry import EncryptionRegistry
from core import EncFileManager

encryptor1 = registry.get_encryptor("xor")
encryptor2 = registry.get_encryptor("fernet")
encryptor3 = registry.get_encryptor("caesar")

manager1 = EncFileManager("vault1", encryptor=encryptor1, compare_by="count")
manager2 = EncFileManager("vault2", encryptor=encryptor2, compare_by="count")
manager3 = EncFileManager("vault3", encryptor=encryptor3, compare_by="count")
manager4 = EncFileManager("vault4", encryptor=encryptor3, compare_by="count")

print(manager1 > manager2)
print(manager4 == manager3)
print(manager1 != manager3)

manager1.compare_by = "size"
manager2.compare_by = "size"

print(manager1 > manager2)
print(manager1 < manager2)

manager1.compare_by = "encryption"
manager2.compare_by = "encryption"
manager3.compare_by = "encryption"

print(manager1 > manager2)
print(manager2 > manager3)

# اختبار الخطأ
# manager1.compare_by = "size"
# manager2.compare_by = "count"
#
# print(manager1 > manager2)

manager1.compare_by = "count"
manager2.compare_by = "count"

print(manager1 >= manager2)
print(manager1 <= manager2)
print(manager1 != manager2)

manager5 = EncFileManager("vault4", encryptor=None, compare_by="encryption")

print(manager4 > manager1)

managers = [manager1, manager2, manager3]

for m in managers:
    m.compare_by = "size"

sorted_list = sorted(managers)

for m in sorted_list:
    print(m)

# merg = manager1 + manager2  # __add__
#
# print(merg)
