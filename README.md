# EncFileManager - Phase 1 (Project Skeleton)

## Course
**OOP - Object-Oriented Programming**  
Instructor: [Alaa Khalaf]

## Project Stage - Phase 1
**This is Phase 1 of the project** – only the basic project skeleton and file handling classes have been implemented.  
Future phases will include encryption, advanced features, and contributions from the team.

## Project Stage - Phase 2
**Phase 2 (Refactor & Stability Improvements)** – The file handling classes have been refactored for better reliability and maintainability.  
Future phases will include encryption, GUI, and advanced features.
### Key Updates
- Replaced string paths with `pathlib.Path` in FileHandler to prevent errors like AttributeError in read().
- Improved folder creation and rename operations to handle non-existing folders and avoid overwriting existing files.
- Added `_safe_path()` method in EncFileManager to prevent access outside the vault folder.
- Unified file extension checks to support additional types (`txt`, `md`, `pdf`).
- Added proper docstrings and comments for clarity.

## Project Stage - Phase 3
**Phase 3 (Simple Encryption Implementation)** – Added basic file encryption/decryption functionality.
### Key Updates
- Introduced `Encryptor` class with Caesar Cipher.
- Added `caesar_encrypt()` and `caesar_decrypt()` methods.
- Demonstrated encryption/decryption for files in the `vault` folder.
- Prepared the code for future extension using inheritance and multiple encryption algorithms.

### Notes
- This phase focuses on understanding encryption logic (strings vs bytes, shifting characters).
- XOR or other algorithms can be added in future phases.
- Current encryption only works on text files (`txt`).

## Project Stage - Phase 4
**Phase 4 (Integration & Encrypted File Handling Extension)** – This phase focuses on integrating encryption logic into the file management system and improving its modularity and usability.
### Key Updates
- Added EncryptedFileHandler class that extends FileHandler to support encrypted read/write operations.
- Integrated the CaesarEncryptor class for simple encryption and decryption of text files.
- Made encryption optional — the handler works in normal or encrypted mode depending on whether an encryptor object is provided.
- Improved code reusability by using super() calls and consistent return values for all I/O operations.
- Added type hints and detailed docstrings for better readability and future maintainability.
- Prepared the project for future integration of multiple encryption algorithms (e.g., XOR, AES).

### Notes
- The encryption system is now fully integrated into the core file management workflow.
- Users can now choose between normal and encrypted file operations without changing the main code logic.
- This phase emphasizes object-oriented design and inheritance-based extensibility.
- Next phases will explore GUI interaction and stronger encryption algorithms.


## Team
- **[Sara Mohammed Abd AL_Zahra]** – Lead Developer & Coordinator
- **[Sara Ahmed]** – Testing Support

## Project Goal
Build a simple file management system in Python to:
- Learn file handling (read, write, delete, rename)
- Practice OOP basics (classes, methods, properties)
- Prepare the project for future encryption features

## Project Structure
EncFileManager/
├── main.py # Main interface ([Sara Mohammed])
├── core.py # Core classes ([Sara Mohammed])
├── encryptor.py # Encryption classes ([Sara Mohammed])
├── test_encryptor.py # Checking encryption classes ([Sara Mohammed])
├── requirements.txt ([Sara Mohammed])
├── README.md ([Sara Mohammed])
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


### Progress - Phase 2

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
