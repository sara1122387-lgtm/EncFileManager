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
├── requirements.txt ([Sara Mohammed])
├── README.md ([Sara Mohammed])
└── .gitignore ([Sara Mohammed])

### Key Updates
**Phase 2:**
- Replaced string paths with `pathlib.Path` in FileHandler to prevent errors like AttributeError in read().
- Improved folder creation and rename operations to handle non-existing folders and avoid overwriting existing files.
- Added `_safe_path()` method in EncFileManager to prevent access outside the vault folder.
- Unified file extension checks to support additional types (`txt`, `md`, `pdf`).
- Added proper docstrings and comments for clarity.

## Getting Started
```bash
# Clone the repository 
git clone [https://github.com/sara1122387-lgtm/EncFileManager.git]

# Install dependencies
pip install -r requirements.txt

# Run the main program
python main.py


Progress - Phase 1

✅ Built project skeleton ([Sara Mohammed])
✅ Created FileHandler & EncFileManager classes ([Sara Mohammed])
✅ Implemented basic file operations ([Sara Mohammed])


Progress - Phase 2

✅ Refactored FileHandler to use pathlib.Path ([Sara Mohammed])  
✅ Enhanced EncFileManager with _safe_path() for security ([Sara Mohammed])  
✅ Unified file extension validation ([Sara Mohammed])  
✅ Added comments and docstrings for clarity ([Sara Mohammed])


 Author / License
Lead Developer & Owner: Sara Mohammed Abd AL_Zahra  
All code and documentation are authored by Sara Mohammed unless otherwise noted.  

Recommended license for public GitHub: MIT License or Creative Commons for documentation.

Notes
This is an educational project built step-by-step for learning purposes.
Future phases will include encryption, GUI, and advanced features.