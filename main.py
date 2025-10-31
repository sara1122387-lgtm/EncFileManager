from core import FileHandler, EncFileManager

# ==========================
# اختبار FileHandler
# ==========================

# التحقق من دالة is_valid_extension
print(FileHandler.is_valid_extension('file.txt'))      # True
print(FileHandler.is_valid_extension('document'))      # False

# إنشاء كائن FileHandler (Path يتحول داخل __init__)
file = FileHandler("vault/test.txt")

# كتابة نص
file.write("Hello world!")

# قراءة النص
print("Content:", file.read())

# تغيير الاسم إلى اسم جديد
try:
    file.rename("vault/hello.txt")
except FileExistsError:
    print("Cannot rename: target file already exists")

# قراءة النص بعد التغيير
print("Content after rename:", file.read())

# حذف الملف
file.delete()

# ==========================
# اختبار EncFileManager
# ==========================
vault = EncFileManager()

# إضافة ملفات
vault.add_file("test1.txt", "Hello Vault!")
vault.add_file("test2.txt", "Second file content")

# عرض الملفات
print("Files in vault:", vault.list_files())

# قراءة محتوى ملف
print("Content of test1.txt:", vault.read_file("test1.txt"))

# حذف ملف
vault.delete_file("test1.txt")
print("Files after deletion:", vault.list_files())

# عدد الملفات
print("Number of files in vault:", vault.file_count)

# ==========================
# اختبار إضافة ملفات صحيحة وخاطئة
# ==========================
# إضافة ملف صحيح الامتداد
vault.add_file("test.txt", "Hello world!")

# محاولة إضافة ملف خاطئ الامتداد
vault.add_file("badfile.exe", "Should not work")

# قراءة الملف
content = vault.read_file("test.txt")
print("Content read:", content)

# حذف الملف
vault.delete_file("test.txt")

# محاولة قراءة بعد الحذف لتأكيد أن الملف اختفى
content_after_delete = vault.read_file("test.txt")
print("Content after delete:", content_after_delete)
