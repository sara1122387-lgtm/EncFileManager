from typing import Optional
from pathlib import Path


class FileHandler:
    def __init__(self, file_path):
        self._file_path = Path(file_path)

    def _ensure_folder_exists(self):
        folder = Path(self._file_path).parent
        folder.mkdir(parents=True, exist_ok=True)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, new_path):
        self._file_path = new_path

    @staticmethod
    def is_valid_extension(file_name: str, extensions=None) -> bool:
        """نتيجة هذه الدالة ستكون boolean"""
        if extensions is None:
            extensions = ['TXT','MD', 'PDF']
        suffix = Path(file_name).suffix.lstrip('.').lower()
        return bool(suffix) and suffix in [e.lower() for e in extensions]

    @classmethod
    def full_path(cls,folder,file_name):
        return str(Path(folder) / file_name)

    def read(self) -> Optional[str]:
        """يرجع محتوى الملف و اذا لم يوجد يرجع None"""
        if not self._file_path.is_file():
            return None
        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f'Error reading file: {e}')
            return None

    def write(self, content: str) -> bool:
        """اذا نجح يرجع True اذا فشل يرجع False"""
        try:
            self._ensure_folder_exists()
            with open(self._file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f'Error writing file: {e}')
            return False

    def rename(self, new_path):
        path = Path(self._file_path)
        if path.exists():
            new_path = Path(new_path)
            new_path.parent.mkdir(parents=True, exist_ok=True)
            if new_path.exists():
                raise FileExistsError(f"Cannot rename: {new_path} already exists")
            path.rename(new_path)
            self._file_path = new_path
        else:
            raise FileNotFoundError(f"No file to rename at {self._file_path}")

    def delete(self) -> bool:
        """اذا نجح يرجع True اذا فشل يرجع False"""
        path = Path(self._file_path)
        try:
            if path.is_file():
                path.unlink()  # لحذف الملف
                return True
            return False #الملف غير موجود
        except Exception as e:
            print(f'Error deleting file: {e}')
            return False



class EncFileManager:
    def __init__(self, vault_folder='vault', encryptor=None):
        self.vault_folder = Path(vault_folder).resolve()
        self.vault_folder.mkdir(parents=True, exist_ok=True)
        self.encryptor = encryptor

    def _safe_path(self, file_name: str) ->Path:
        """تحقق من أن الملف داخل مجلد vault فقط"""
        file_path = (self.vault_folder / file_name).resolve()
        if not str(file_path).startswith(str(self.vault_folder)):
            raise ValueError("Access outside vault folder is not allowed")
        return file_path

    def list_files(self) -> list:
        """إرجاع قائمة الملفات (قد تكون فارغة)."""
        try:
            return [f.name for f in self.vault_folder.iterdir() if f.is_file()]
        except Exception as e:
            print(f'Error listing files: {e}')
            return []

    def add_file(self, file_name: str, content:str ="") -> bool:
        """اضافة ملف جديد داخل vault"""
        file_path = self._safe_path(file_name)

        # تحقق من الامتداد
        if not FileHandler.is_valid_extension(file_name):
            print("Invalid file extension!")
            return False

        data = content.encode("utf-8")

        if self.encryptor:
            data = self.encryptor.encrypt(data)

        try:
            with open(file_path, "wb") as f:
                f.write(data)
            return True
        except Exception:
            return False

        # استخدام EncryptedFileHandler إذا تم تمرير encryptor

    def read_file(self, file_name: str) -> Optional[str]:
        """قراءة محتوى ملف محدد"""
        file_path = self._safe_path(file_name)

        try:
            with open(file_path, "rb") as f:
                data= f.read()

            if self.encryptor:
                data = self.encryptor.decrypt(data)

            return data.decode("utf-8")
        except Exception:
            return None


    def delete_file(self, file_name: str) ->bool:
        file_path = self._safe_path(file_name)
        handler = FileHandler(file_path)
        return handler.delete()  # boolean


    @property
    def file_count(self):
        """ارجاع عدد الملفات في المجلد وقمت بها بسبب سهولة الاستخدام و اضافة ميزات مع امكانية تعديل و الامان لاننا لم نعرف setter"""
        return len(self.list_files())















