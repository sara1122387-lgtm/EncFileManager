# interface.py

from core import EncFileManager


class CLI:
    def __init__(self, registry):
        self.registry = registry
        self.manager = None

        #  System State (بديل current_vault + current_pipeline)
        self.state = {
            "vault": None,
            "pipeline": None
        }

    # ========= MAIN =========
    def run(self):
        while True:
            self._print_main_menu()
            choice = input("Select: ")

            if choice == "1":
                self.file_management()

            elif choice == "2":
                self.pipeline_builder()

            elif choice == "3":
                self.compare_managers()

            elif choice == "4":
                self.demos()

            elif choice == "0":
                print("Exit 👋")
                break

            else:
                print("Invalid option, try again.")

    # ========= MENUS =========
    def _print_main_menu(self):
        print("\n=== SYSTEM MENU ===")
        print("1) File Management")
        print("2) Build Pipeline")
        print("3) Compare Vaults")
        print("4) Advanced Features")
        print("0) Exit")

    # ========= FILE =========
    def file_management(self):
        enc = self._choose_encryptor()

        self.manager = EncFileManager("user_vault", encryptor=enc)

        #  update state
        self.state["vault"] = "user_vault"

        while True:
            print("\n1) Add File\n2) Read File\n3) Delete File\n4) List\n0) Back")
            c = input("Choose: ")
            ALLOWED_EXTENSIONS = (".txt", ".md", ".pdf")

            if c == "1":
                name = input("Name: ")
                content = input("Content: ")
                if not name.lower().endswith(ALLOWED_EXTENSIONS):
                    print("Invalid file type. Allowed: txt, md, pdf")
                    return False
                print(self.manager.add_file(name, content))

            elif c == "2":
                name = input("Name: ")
                if not name.lower().endswith(ALLOWED_EXTENSIONS):
                    print("Invalid file type. Allowed: txt, md, pdf")
                    return False
                print(self.manager.read_file(name))

            elif c == "3":
                name = input("Name: ")
                if not name.lower().endswith(ALLOWED_EXTENSIONS):
                    print("Invalid file type. Allowed: txt, md, pdf")
                    return False
                print(self.manager.delete_file(name))

            elif c == "4":
                print(self.manager.list_files())

            elif c == "0":
                break

            else:
                print("Invalid option, try again.")

    # ========= PIPELINE =========
    def pipeline_builder(self):
        print("\nBuild Pipeline (type 'done' to finish)")

        pipeline = None

        while True:
            name = input("Encryptor: ").lower()

            if name == "done":
                break

            try:
                enc = self.registry.get_encryptor(name)
            except ValueError:
                print("Encryptor not found, skipped")
                continue

            if pipeline is None:
                pipeline = enc
            else:
                pipeline = pipeline | enc

        #  store pipeline in state
        self.state["pipeline"] = pipeline

        print("Final Pipeline:", pipeline)

        self.manager = EncFileManager("pipeline_vault", encryptor=pipeline)

        #  update vault state
        self.state["vault"] = "pipeline_vault"

        print("Current Vault:", self.state["vault"])
        print("Current Pipeline:", self.state["pipeline"])

    # ========= COMPARE =========
    def compare_managers(self):
        print("\n=== Compare Vaults ===")

        e1 = self._choose_encryptor()
        e2 = self._choose_encryptor()

        m1 = EncFileManager("v1", encryptor=e1)
        m2 = EncFileManager("v2", encryptor=e2)

        mode = input("Compare by (count/size/encryption): ")
        m1.compare_by = mode
        m2.compare_by = mode

        print("m1 > m2:", m1 > m2)

    # ========= DEMOS =========
    def demos(self):
        print("\n1) Pointer\n2) Friend Function\n0) Back")
        c = input("Choose: ")

        if c == "1":
            enc = self.registry.get_encryptor("xor")

            m1 = EncFileManager("v1", encryptor=enc)
            m2 = EncFileManager("v2", encryptor=enc)

            print("Same object:", m1.encryptor is m2.encryptor)

            #  إظهار أثر الـ pointer (مهم جدًا!)
            enc.key = 99
            print("m1 key:", m1.encryptor.key)
            print("m2 key:", m2.encryptor.key)

        elif c == "2":
            manager = EncFileManager("v")
            manager.add_file("t.txt", "hi")

            handler = manager._get_handler("t.txt")

            from utils import inspect_file
            print(inspect_file(handler))

    # ========= HELPER =========
    def _choose_encryptor(self):
        name = input("Encryptor (caesar/xor/fernet/none): ").lower()

        valid = ["caesar", "xor", "fernet", "none"]

        if name not in valid:
            print("Invalid encryptor! default = none")
            return None

        if name == "none":
            return None

        return self.registry.get_encryptor(name)