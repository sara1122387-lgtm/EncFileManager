#core.py

from typing import Optional
from pathlib import Path


class FileHandler:
    def __init__(self, file_path):
        self._file_path = Path(file_path)

    def _ensure_folder_exists(self):
        self._file_path.parent.mkdir(parents=True, exist_ok=True)

    @property
    def file_path(self):
        return self._file_path

    def read(self) -> Optional[bytes]:
        """يرجع محتوى الملف و اذا لم يوجد يرجع None"""
        if not self._file_path.is_file():
            return None
        try:
            with open(self._file_path, 'rb') as f:
                return f.read()
        except Exception:
            return None

    def write(self, data: bytes) -> bool:
        """اذا نجح يرجع True اذا فشل يرجع False"""
        try:
            self._ensure_folder_exists()
            with open(self._file_path, 'wb') as f:
                f.write(data)
            return True
        except Exception:
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
        except Exception:
            return False



    def __repr__(self):
        return f"<FileHandler path={self.file_path}>"

    def __eq__(self, other):
        if isinstance(other, FileHandler):
            return self.file_path == other.file_path
        return False

from functools import total_ordering
@total_ordering
class EncFileManager:
    from base_encryptor import BaseEncryptor
    ALLOWED_EXTENSIONS = (".txt", ".md", ".pdf")
    def __init__(self, vault_folder='vault', encryptor: BaseEncryptor = None, compare_by="count"):
        self.vault_folder = Path(vault_folder).resolve()
        self.vault_folder.mkdir(parents=True, exist_ok=True)
        self.encryptor = encryptor
        self.compare_by = compare_by

    #Added
    def _get_handler(self, file_name: str) -> FileHandler:
        file_path = self._safe_path(file_name)
        return FileHandler(file_path)

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
        # تحقق من الامتداد
        if not file_name.lower().endswith(self.ALLOWED_EXTENSIONS):
            return False

        handler = self._get_handler(file_name)

        data = content.encode("utf-8")

        if self.encryptor:
            data = self.encryptor.encrypt(data)

        return handler.write(data)


    def read_file(self, file_name: str) -> Optional[str]:
        """قراءة محتوى ملف محدد"""
        handler = self._get_handler(file_name)
        data = handler.read()

        if data is None:
            return None

        if self.encryptor:
            data = self.encryptor.decrypt(data)
        return data.decode("utf-8")

    #Modified
    def delete_file(self, file_name: str) -> bool:
        handler = self._get_handler(file_name)
        return handler.delete()

    def _total_size(self):
        total = 0
        for file in self.list_files():
            path = Path(file)
            if path.exists():
                total += path.stat().st_size
        return total

    def _encryption_rank(self):
        if not self.encryptor:
            return 0
        ranks = {
            "caesar": 1,
            "xor": 2,
            "fernet": 3
        }
        return ranks.get(self.encryptor.name.lower(), 0)

    def _comparison_value(self):
        if self.compare_by == "count":
            return len(self)

        elif self.compare_by == "size":
            return self._total_size()

        elif self.compare_by == "encryption":
            return self._encryption_rank()

        else:
            return 0

    def __getitem__(self, file_name):
        return self.read_file(file_name)

    def __setitem__(self, file_name, content):
        self.add_file(file_name, content)

    def __contains__(self, file_name):
        try:
            handler = self._get_handler(file_name)
            return handler.file_path.is_file()
        except ValueError:
            return False

    def __str__(self):
        return f"[Vault: {len(self)} files]"

    def __add__(self, other):
        if not isinstance(other, EncFileManager):
            return NotImplemented

        new_manager = EncFileManager(vault_folder="merged_vault")

        for file_name in self.list_files():
            content = self.read_file(file_name)
            if content:
                new_manager.add_file(file_name, content)

        for file_name in other.list_files():
            if file_name not in new_manager.list_files():
                content = other.read_file(file_name)
                if content:
                    new_manager.add_file(file_name, content)

        return new_manager


    def __len__(self):
        return len(self.list_files())

    def __eq__(self, other):
        if not isinstance(other, EncFileManager):
            return NotImplemented

        if self.compare_by != other.compare_by:
            raise ValueError("Cannot compare with different comparison modes")
        return self._comparison_value() == other._comparison_value()

    def __lt__(self, other):
        if not isinstance(other, EncFileManager):
            return NotImplemented
        if self.compare_by != other.compare_by:
            raise ValueError("Cannot compare with different comparison modes")
        return self._comparison_value() < other._comparison_value()


