from cryptography.fernet import Fernet
import os

class FileHandler:
    def __init__(self, file_path):
        self._file_path = file_path

    def _ensure_folder_exists(self):
        folder = os.path.dirname(self._file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, new_path):
        self._file_path = new_path

    @staticmethod
    def is_valid_extension(file_name, extension=None):
        if extension is None:
            extension = ['txt','md']
        ext = file_name.split('.')[-1]
        return ext in extension

    @classmethod
    def full_path(cls,folder,file_name):
        return os.path.join(folder,file_name)

    def read(self):
        if not os.path.isfile(self._file_path):
            return None
        with open(self._file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def write(self, content):
        self._ensure_folder_exists()
        with open(self._file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def rename(self, new_path):
        if os.path.exists(self._file_path):
            folder = os.path.dirname(new_path)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)
            os.rename(self._file_path, new_path)
            self._file_path = new_path
        else:
            raise FileNotFoundError(f"No file to rename at {self._file_path}")

    def delete(self):
        if os.path.isfile(self._file_path):
            os.remove(self._file_path)
        else:
            print(f"Warning: File does not exist: {self._file_path}")



class EncFileManager:
    def __init__(self, vault_folder='vault'):
        self.vault_folder = vault_folder
        if not os.path.exists(self.vault_folder):
            os.makedirs(self.vault_folder, exist_ok=True)

    def list_files(self):
        """ارجاع قائمة الملفات في مجلد vault"""
        return [f for f in os.listdir(self.vault_folder) if os.path.isfile(os.path.join(self.vault_folder, f))]

    def add_file(self, file_name, content=""):
        """اضافة ملف جديد داخل vault"""
        if not FileHandler.is_valid_extension(file_name, ["txt", "md"]):
            print("Invalid file extension!")
            return None
        return FileHandler(os.path.join(self.vault_folder, file_name)).write(content)

    def read_file(self, file_name):
        """قراءة محتوى ملف محدد"""
        try:
            return FileHandler(os.path.join(self.vault_folder, file_name)).read()
        except FileNotFoundError:
            print(f"File {file_name} not found!")
            return ""

    def delete_file(self, file_name):
        path = os.path.join(self.vault_folder, file_name)
        if os.path.isfile(path):
            FileHandler(path).delete()
        else:
            print(f"Warning: {file_name} does not exist.")


    @property
    def file_count(self):
        """ارجاع عدد الملفات في المجلد وقمت بها بسبب سهولة الاستخدام و اضافة ميزات مع امكانية تعديل و الامان لاننا لم نعرف setter"""
        return len(self.list_files())




















