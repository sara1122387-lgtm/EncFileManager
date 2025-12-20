# **EncFileManager**

## Course
**OOP - Object-Oriented Programming**  
Instructor: [Alaa Khalaf]

### Project Stage - Phase 1
**This is Phase 1 of the project** – only the basic project skeleton and file handling classes have been implemented.  
Future phases will include encryption, advanced features, and contributions from the team.

### Project Stage - Phase 2
**Phase 2 (Refactor & Stability Improvements)** – The file handling classes have been refactored for better reliability and maintainability.  
Future phases will include encryption, GUI, and advanced features.
#### Key Updates
- Replaced string paths with `pathlib.Path` in FileHandler to prevent errors like AttributeError in read().
- Improved folder creation and rename operations to handle non-existing folders and avoid overwriting existing files.
- Added `_safe_path()` method in EncFileManager to prevent access outside the vault folder.
- Unified file extension checks to support additional types (`txt`, `md`, `pdf`).
- Added proper docstrings and comments for clarity.

### Project Stage - Phase 3
**Phase 3 (Simple Encryption Implementation)** – Added basic file encryption/decryption functionality.
#### Key Updates
- Introduced `Encryptor` class with Caesar Cipher.
- Added `caesar_encrypt()` and `caesar_decrypt()` methods.
- Demonstrated encryption/decryption for files in the `vault` folder.
- Prepared the code for future extension using inheritance and multiple encryption algorithms.

#### Notes
- This phase focuses on understanding encryption logic (strings vs bytes, shifting characters).
- XOR or other algorithms can be added in future phases.
- Current encryption only works on text files (`txt`).

### Project Stage - Phase 4
**Phase 4 (Integration & Encrypted File Handling Extension)** – This phase focuses on integrating encryption logic into the file management system and improving its modularity and usability.
#### Key Updates
- Added EncryptedFileHandler class that extends FileHandler to support encrypted read/write operations.
- Integrated the CaesarEncryptor class for simple encryption and decryption of text files.
- Made encryption optional — the handler works in normal or encrypted mode depending on whether an encryptor object is provided.
- Improved code reusability by using super() calls and consistent return values for all I/O operations.
- Added type hints and detailed docstrings for better readability and future maintainability.
- Prepared the project for future integration of multiple encryption algorithms (e.g., XOR, AES).

#### Notes
- The encryption system is now fully integrated into the core file management workflow.
- Users can now choose between normal and encrypted file operations without changing the main code logic.
- This phase emphasizes object-oriented design and inheritance-based extensibility.
- Next phases will explore GUI interaction and stronger encryption algorithms.

### Project Stage - Phase 5
**Phase 5 (Validation, Testing & Internal Utilities)** – This phase focuses on verifying system stability, adding automated checks, and ensuring that all previous phases integrate correctly.
#### Key Updates
- Added SystemValidator class to perform integrity checks on vault folder, file operations, and encryption components. 
- Implemented a simple readiness test to ensure:
  - Required folders exist 
  - FileHandler operations work without throwing exceptions 
- Encryption/decryption pipeline runs successfully 
- Introduced internal utilities for cleaner logging and debug messages. 
- Prepared the project for GUI integration and stronger cryptographic algorithms in the next stage.

#### Notes
- This phase does not introduce new user
- facing features; it strengthens the internal structure. 
- The goal is to confirm that Phase 1–4 are stable, modular, and safe to extend.
- The validation system can be expanded later to include unit tests (pytest) or auto-check scripts.

### Project Stage - Phase 6
**Phase 6 (Polymorphism & Strategy Pattern)** – This phase focuses on professionalizing the encryption system using polymorphism and a strategy pattern, allowing multiple encryption algorithms to be used interchangeably.
#### Key Updates
- Introduced BaseEncryptor interface using ABC (Abstract Base Class) for a common encrypt/decrypt API.
- Refactored CaesarEncryptor to inherit from BaseEncryptor and implement required methods.
- Created XOREncryptor as a new option, inheriting from BaseEncryptor, supporting XOR-based encryption for demonstration.
- Updated FernetEncryptor to implement BaseEncryptor, supporting bytes-based encryption with Fernet (AES-128 + HMAC).
- Modified EncFileManager to use any encryptor via the unified interface:
  - self.encryptor.encrypt(data)
  - self.encryptor.decrypt(data)
- Eliminated tight coupling: EncFileManager no longer depends on specific encryption classes, allowing easy swapping of algorithms.
- Prepared the project for future expansion with additional encryptors or GUI integration.

#### Notes
- This phase emphasizes OOP best practices, clean separation of concerns, and code extensibility.
- Users can switch encryption methods without modifying core file management logic.
- Polymorphism ensures the same EncFileManager code works regardless of the underlying encryption algorithm.
- Future phases may add configuration options to select encryption strategies at runtime.


### Project Completion & Special Methods

**Phase 7 (Finalization & Advanced Python Features)** – This final phase focuses on adding Pythonic enhancements, including special (magic) methods, and consolidating the project into a professional, extensible file management system.
#### Key Updates
- Implemented Special Methods across core classes:
  - __getitem__ and __setitem__ in EncFileManager for dictionary-like file access.
  - __contains__ in EncFileManager to check for file existence using in.
  - __len__ in EncFileManager to quickly get the number of files.
  - __str__ and __repr__ in FileHandler and EncFileManager for readable and unambiguous object representation.
  - Comparison methods (__eq__ and __lt__) in FileHandler to allow file comparisons by name or custom logic.
- Verified full integration of encryption strategies (Caesar, XOR, Fernet) via the unified BaseEncryptor interface.
- Added automated readiness tests confirming:
  - Vault folder integrity
  - File operations (read/write/delete/rename)
  - Encryption/decryption pipeline works correctly for all encryptors
  - Special methods operate as expected

#### Notes
- The project now behaves like a professional Python package: modular, secure, and highly extensible.
- Users can easily switch encryption strategies or extend functionality with minimal changes to core logic.
- The system demonstrates advanced OOP principles: inheritance, polymorphism, abstraction, and operator overloading.
- Future improvements can include GUI integration, dynamic selection of encryption strategies at runtime, and support for additional file types.
  

## Team
- **[Sara Mohammed Abd AL_Zahra]** – Lead Developer & Coordinator
<<<<<<< HEAD
- **[Sara Ahmed]** – Team Member (added for course requirement; no active contributions)
=======
- **[Sara Ahmed]** – Team Member (included as per course requirement)
>>>>>>> 8a69f45859b60abae8816d5bd3eaefeb0bc40c5b

## Project Goal
Create a modular Python file management system that:
- Handles files securely (read, write, delete, rename)
- Demonstrates Object-Oriented Programming principles
- Implements basic encryption to illustrate encryption logic
- Is structured for future expansion with advanced features

## Project Structure
EncFileManager/
├── main.py # Main interface ([Sara Mohammed])
├── core.py # Core classes ([Sara Mohammed])
├── encryptor.py # Encryption classes ([Sara Mohammed])
├── base_encryptor.py ([Sara Mohammed])
├── test_encryptor.py # Checking encryption classes ([Sara Mohammed])
├── requirements.txt ([Sara Mohammed])
├── README.md ([Sara Mohammed])
├── FernetEncryptor.py ([Sara Mohammed])
├── test_phase5.py ([Sara Mohammed])
├── test_phase6.py ([Sara Mohammed])
└── .gitignore ([Sara Mohammed])


### Progress - Phase 1

✅ Built project skeleton ([Sara Mohammed])
✅ Created FileHandler & EncFileManager classes ([Sara Mohammed])
✅ Implemented basic file operations ([Sara Mohammed])


### Progress - Phase 2

✅ Refactored FileHandler to use pathlib.Path ([Sara Mohammed])  
✅ Enhanced EncFileManager with _safe_path() for security ([Sara Mohammed])  
✅ Unified file extension validation ([Sara Mohammed])  
✅ Added comments and docstrings for clarity ([Sara Mohammed])


### Progress - Phase 3

✅ Created Encryptor class implementing Caesar Cipher ([Sara Mohammed])
✅ Added caesar_encrypt() and caesar_decrypt() methods ([Sara Mohammed])
✅ Tested encryption and decryption on files within the vault folder ([Sara Mohammed])
✅ Structured project for future integration with core classes via inheritance ([Sara Mohammed])
✅ Documented encryption logic and usage notes in code comments ([Sara Mohammed])


### Progress - Phase 4

✅ Created EncryptedFileHandler class ([Sara Mohammed])
✅ Integrated encryption functionality with FileHandler ([Sara Mohammed])
✅ Improved flexibility and optional encryption use ([Sara Mohammed])
✅ Added detailed comments, docstrings, and type hints ([Sara Mohammed])


### Progress - Phase 5

✅ Implemented FernetEncryptor class using Fernet (AES-128 + HMAC) for real encryption ([Sara Mohammed])
✅ Added secure key generation and automatic loading/saving of encryption keys ([Sara Mohammed])
✅ Updated EncFileManager to support pluggable encryption via encryptor=FernetEncryptor() ([Sara Mohammed])
✅ Modified file operations to handle bytes-based encryption instead of plain text ([Sara Mohammed])
✅ Added readiness test ensuring folder structure, FileHandler stability, and full encryption/decryption pipeline validation ([Sara Mohammed])
✅ Documented encryption workflow, key handling, and integration notes for future contributors ([Sara Mohammed])

### Progress - Phase 6

✅ Implemented BaseEncryptor interface using ABC for a unified encryption API ([Sara Mohammed])
✅ Refactored CaesarEncryptor to inherit from BaseEncryptor ([Sara Mohammed])
✅ Created XOREncryptor class as an alternative encryption strategy ([Sara Mohammed])
✅ Updated FernetEncryptor to implement BaseEncryptor ([Sara Mohammed])
✅ Modified EncFileManager to use polymorphism: support multiple encryption algorithms via strategy pattern ([Sara Mohammed])
✅ Tested all encryptors with EncFileManager ensuring encryption/decryption works interchangeably ([Sara Mohammed])
✅ Documented strategy pattern usage, class hierarchy, and guidelines for adding new encryptors ([Sara Mohammed])

### Progress – Final Phase
✅ Implemented dictionary-like access for files in EncFileManager ([Sara Mohammed])
✅ Added file existence checking, length reporting, and readable object representations ([Sara Mohammed])
✅ Enabled file comparisons using equality and ordering operators ([Sara Mohammed])
✅ Verified full interoperability with all encryptors ([Sara Mohammed])
✅ Added automated internal tests for readiness and Special Methods ([Sara Mohammed])
✅ Documented class hierarchy, usage of magic methods, and guidelines for extension ([Sara Mohammed])



 ## Author / License
**Lead Developer & Owner:** Sara Mohammed Abd AL_Zahra  
All code and documentation are authored by Sara Mohammed unless otherwise noted.  
Recommended license for public GitHub: MIT License or Creative Commons for documentation.

---

Notes
This is an educational project built step-by-step for learning purposes.
Future phases will include encryption, GUI, and advanced features.

## Getting Started
```bash
# Clone the repository 
git clone [https://github.com/sara1122387-lgtm/EncFileManager.git]

# Install dependencies
pip install -r requirements.txt

# Run the main program
python main.py
