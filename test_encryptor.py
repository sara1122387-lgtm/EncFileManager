from encryptor import CaesarEncryptor
from core import EncFileManager

vault = EncFileManager()
encryptor =  CaesarEncryptor(key=3)


for file_name in vault.list_files():
    content = vault.read_file(file_name)
    if content:
        encrypted = encryptor.caesar_encrypt(content, encryptor.key)
        decrypted = encryptor.caesar_decrypt(encrypted, encryptor.key)
        print(f"\nFile: {file_name}")
        print("Original:", content)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)

# enc = CaesarEncryptor(key=3)
#
# text = "Hello Sara!"
# encrypted = enc.caesar_encrypt(text, enc.key)
# decrypted = enc.caesar_decrypt(encrypted, enc.key)
#
# print('original:', text)
# print('Encrypted:', encrypted)
# print('Decrypted:', decrypted)

# vault = EncFileManager()
#
# # اختر ملف موجود داخل vault
# file_name = "hello.txt"  # أو "test2.txt"
#
#
# #قراءة المحتوى
# content = vault.read_file(file_name)
# if content is None:
#     print(f"File {file_name} could not be read or is empty.")
# else:
#     print("Original content:", content)
#
# encryptor =  CaesarEncryptor(key=3)
#
# # تشفير
# encrypted = encryptor.caesar_encrypt(content, encryptor.key)
# print("Encrypted:", encrypted)
#
# # فك التشفير للتأكد
# decrypted = encryptor.caesar_decrypt(encrypted, encryptor.key)
# print("Decrypted:", decrypted)








