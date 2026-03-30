from core import FileHandler


def inspect_file(handler: FileHandler):
    """
    Simulates a 'friend function' by accessing FileHandler internals.
    """
    path = handler.file_path
    exists = path.exists()

    return {
        "path": str(path),
        "exists": exists
    }