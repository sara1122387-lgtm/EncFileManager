from core import EncFileManager
from encryptors import CaesarEncryptor, XOREncryptor
from FernetEncryptor import FernetEncryptor


def choose_encryptor():
    print("\nChoose encryption type:")
    print("1) Caesar Cipher")
    print("2) XOR Cipher")
    print("3) Fernet (Secure)")
    choice = input("Your choice: ")

    if choice == '1':
        key = int(input("Enter key value (e.g. 3): "))
        return CaesarEncryptor(key)

    elif choice == '2':
        key = int(input("Enter key value (e.g. 42): "))
        return XOREncryptor(key)

    elif choice == '3':
        return FernetEncryptor()

    else:
        print("Invalid choice, encryption disabled")
        return None


def main():
    print("=== EncFileManager ===")

    use_encryption = input("Do you want to use encryption? (y/n): ").lower() == 'y'
    encryptor = choose_encryptor() if use_encryption else None

    manager = EncFileManager(encryptor=encryptor)

    while True:
        print("\nMenu:")
        print("1) Add file")
        print("2) Read file")
        print("3) Delete file")
        print("4) List files")
        print("5) Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("File name: ")
            content = input("File content: ")
            if manager.add_file(name, content):
                print("File added successfully")
            else:
                print("Failed to add file")

        elif choice == '2':
            name = input("File name: ")
            content = manager.read_file(name)
            if content is not None:
                print("\n--- File Content ---")
                print(content)
            else:
                print("Unable to read file")

        elif choice == '3':
            name = input("File name: ")
            if manager.delete_file(name):
                print("File deleted successfully")
            else:
                print("File deletion failed")

        elif choice == '4':
            files = manager.list_files()
            print("\nFiles in vault:")
            for f in files:
                print("-", f)

        elif choice == '5':
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
