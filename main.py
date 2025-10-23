from core import FileHandler, EncFileManager

#Examples to verify the codes work

# file = FileHandler("vault/test.txt")
#
# # كتابة نص
# file.write("Hello world!")
#
# # قراءة النص
# print("Content:", file.read())
#
# # تغيير الاسم (اختياري الآن)
# file.rename("vault/hello.txt")
#
# # قراءة النص بعد التغيير
# print("Content after rename:", file.read())
#
# # حذف الملف
# file.delete()


# vault = EncFileManager()
#
# # إضافة ملف
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


# vault = EncFileManager()
#
# # محاولة إضافة ملف صحيح الامتداد
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
