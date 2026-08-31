# EncFileManager

**EncFileManager** is a modular Python-based file vault that combines controlled file management with pluggable encryption strategies.

The project explores practical applications of object-oriented design, abstraction, polymorphism, strategy-based architecture, operator overloading, and composable encryption pipelines within a small, self-contained system.

Rather than coupling the file manager to a specific encryption algorithm, the architecture allows encryption strategies to be exchanged, registered, and composed without modifying the core file-management logic.

> **Project Status:** Functional CLI-based implementation with multiple encryption strategies, dynamic strategy registration, and composable encryption pipelines.

---

## Overview

EncFileManager provides an isolated **Vault** environment where file operations are performed through a controlled interface.

The system supports:

* File creation and writing
* File reading
* File deletion
* File renaming
* File listing
* Vault-level file counting
* Controlled path resolution
* Optional encryption
* Multiple interchangeable encryption strategies
* Runtime encryption strategy selection
* Composable encryption pipelines
* Vault comparison using overloaded operators
* Dictionary-like access to files
* CLI-based interaction

The project was developed incrementally, evolving from basic file handling into a more extensible object-oriented architecture.

---

## Architecture

The core architecture separates file management from encryption.

```text
                         ┌─────────────────────┐
                         │       CLI / UI       │
                         │     interface.py    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  EncFileManager     │
                         │       core.py       │
                         └───────┬─────┬───────┘
                                 │     │
                    ┌────────────┘     └─────────────┐
                    ▼                                ▼
             ┌──────────────┐               ┌─────────────────┐
             │ FileHandler  │               │ BaseEncryptor   │
             │              │               │      (ABC)      │
             └──────┬───────┘               └────────┬────────┘
                    │                                │
                    ▼                    ┌───────────┼───────────┐
              File System                ▼           ▼           ▼
                                      Caesar        XOR        Fernet
                                                   
                                      └─────────────┬─────────────┘
                                                    │
                                                    ▼
                                         EncryptionPipeline
```

### Main Components

#### `FileHandler`

Responsible for low-level file operations:

* Read
* Write
* Rename
* Delete
* File path management

File content is handled as bytes, allowing the same file-handling layer to work with different encryption strategies.

#### `EncFileManager`

Acts as the main vault-level abstraction.

Responsibilities include:

* Vault creation and management
* Path validation
* File operations
* Optional encryption/decryption
* Encryption strategy integration
* File collection behavior
* Vault comparison
* Operator overloading

#### `BaseEncryptor`

An abstract interface defining a common encryption contract:

```python
encrypt(data: bytes) -> bytes
decrypt(data: bytes) -> bytes
```

This abstraction allows different encryption implementations to be used interchangeably.

#### `EncryptionRegistry`

Provides dynamic registration and lookup of encryption strategies.

Strategies can be retrieved by name instead of being hard-coded into the file manager.

#### `EncryptionPipeline`

Allows multiple encryption strategies to be composed into a sequential pipeline.

For example:

```python
pipeline = caesar | xor | fernet
```

Encryption is applied from left to right, while decryption reverses the sequence.

---

## Encryption Strategies

### Caesar

A simple byte-shifting implementation.

```text
Purpose:
Educational demonstration of encryption concepts.

Security:
Not suitable for protecting real confidential data.
```

### XOR

A simple XOR-based implementation.

```text
Purpose:
Educational demonstration of symmetric transformation and
interchangeable encryption strategies.

Security:
Not suitable for protecting real confidential data.
```

### Fernet

The project also integrates Fernet through the `cryptography` library.

Fernet provides authenticated symmetric encryption and is the project's practical cryptographic option.

The implementation also supports:

* Automatic key generation
* Persistent key storage
* Loading an existing key
* Byte-based encryption/decryption

> **Important:** The security of a real deployment depends on appropriate key management. Encryption keys should never be committed to a public repository.

---

## Encryption Pipeline

One of the main architectural features is composable encryption.

Because encryption strategies inherit from `BaseEncryptor`, they can be combined using the `|` operator:

```python
pipeline = caesar | xor | fernet
```

The resulting flow is:

```text
Original Data
     │
     ▼
  Caesar
     │
     ▼
    XOR
     │
     ▼
   Fernet
     │
     ▼
Encrypted Data
```

During decryption, the pipeline automatically reverses the order:

```text
Encrypted Data
     │
     ▼
   Fernet
     │
     ▼
    XOR
     │
     ▼
  Caesar
     │
     ▼
Original Data
```

This demonstrates how operator overloading can be combined with polymorphism to create a composable API.

---

## Dynamic Encryption Registry

Encryption strategies are registered through `EncryptionRegistry`.

```python
registry = EncryptionRegistry()

registry.register(CaesarEncryptor())
registry.register(XOREncryptor())
registry.register(FernetEncryptor())
```

Strategies can then be resolved dynamically:

```python
encryptor = registry.get_encryptor("fernet")
```

This keeps `EncFileManager` independent from individual encryption implementations.

The design also makes it possible to introduce additional strategies without rewriting the core file-management logic.

---

## Object-Oriented Design

The project demonstrates several object-oriented and Python-specific concepts.

### Abstraction

`BaseEncryptor` defines a common interface for all encryption strategies.

### Inheritance

Concrete encryptors inherit from `BaseEncryptor`.

```text
BaseEncryptor
    ├── CaesarEncryptor
    ├── XOREncryptor
    ├── FernetEncryptor
    └── EncryptionPipeline
```

### Polymorphism

`EncFileManager` interacts with encryption objects through the shared interface:

```python
self.encryptor.encrypt(data)
self.encryptor.decrypt(data)
```

The manager does not need to know which concrete strategy is being used.

### Operator Overloading

The project uses Python's data model to provide intuitive operations.

Examples include:

```python
manager["file.txt"]
manager["file.txt"] = "content"

"file.txt" in manager

len(manager)

manager1 < manager2
manager1 == manager2
manager1 + manager2
```

Encryption pipelines also use:

```python
caesar | xor | fernet
```

### `@total_ordering`

`EncFileManager` uses `@total_ordering` to support comparison based on configurable metrics.

Available comparison modes include:

* `count`
* `size`
* `encryption`

### Shared Object References

The CLI includes a demonstration of Python's object-reference behavior by allowing multiple managers to reference the same encryptor instance.

### External Inspection Utility

`utils.py` contains an external inspection function that demonstrates a friend-like utility approach for accessing information associated with a `FileHandler` without making the function a class method.

---

## Vault Isolation

The project includes controlled path resolution through `_safe_path()`.

File paths are resolved relative to the configured vault directory before file operations are performed.

The intended security property is to prevent file operations from escaping the vault through path traversal attempts.

The implementation is designed around the principle:

```text
Requested Path
      │
      ▼
Resolve Absolute Path
      │
      ▼
Validate Against Vault
      │
 ┌────┴────┐
 │         │
Inside    Outside
 │         │
 ▼         ▼
Allow     Reject
```

This addresses the class of path traversal concerns commonly associated with **CWE-22**.

> This project is an educational implementation and should not be considered a production-grade security boundary without further security review and hardening.

---

## Command-Line Interface

The project currently provides an interactive CLI through `interface.py`.

The main menu provides access to:

```text
1) File Management
2) Build Pipeline
3) Compare Vaults
4) Advanced Features
0) Exit
```

### File Management

Supports:

* Selecting an encryption strategy
* Adding files
* Reading files
* Deleting files
* Listing files

### Pipeline Builder

Allows users to construct an encryption pipeline interactively by selecting registered encryption strategies.

### Vault Comparison

Vault managers can be compared using:

* File count
* Total size
* Encryption rank

### Advanced Features

The CLI also demonstrates:

* Shared object references
* External inspection utilities
* Python operator behavior

---

## Testing

The project includes several standalone test scripts covering different aspects of the system.

### `test_encryptor.py`

Focused on encryption/decryption correctness across the available encryption strategies and the encryption pipeline.

### `test_integration.py`

Tests integration between encryption strategies and `EncFileManager`, including:

* File creation
* File existence
* File counting
* Reading and decryption
* File deletion
* Post-deletion verification

The integration flow is exercised with:

* No encryption
* Caesar
* XOR
* Fernet

### `test_phase5.py`

Focuses on Fernet integration and verifies that encrypted content is not stored as the original plaintext.

### `test_phase6.py`

Exercises the unified encryption interface across Caesar, XOR, and Fernet while testing the main file-management workflow.

The tests are currently implemented as lightweight Python test scripts rather than a full `pytest` suite.

---

## Project Structure

```text
EncFileManager/
│
├── main.py
├── interface.py
│
├── core.py
├── base_encryptor.py
├── encryptors.py
├── FernetEncryptor.py
├── pipeline.py
├── encryption_registry.py
├── utils.py
│
├── test_encryptor.py
├── test_integration.py
├── test_phase5.py
├── test_phase6.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sara1122387-lgtm/EncFileManager.git
cd EncFileManager
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

---

## Basic Usage

A manager can operate without encryption:

```python
manager = EncFileManager("vault")

manager.add_file("example.txt", "Hello EncFileManager!")
print(manager.read_file("example.txt"))
```

Or with an encryption strategy:

```python
encryptor = FernetEncryptor()

manager = EncFileManager(
    "vault",
    encryptor=encryptor
)

manager.add_file("secret.txt", "Confidential content")
print(manager.read_file("secret.txt"))
```

A pipeline can also be used:

```python
pipeline = (
    CaesarEncryptor()
    | XOREncryptor()
    | FernetEncryptor()
)

manager = EncFileManager(
    "pipeline_vault",
    encryptor=pipeline
)
```

---

## Security Considerations

EncFileManager is primarily an **educational and architectural project**.

Important considerations:

* Caesar and XOR are demonstration algorithms and should not be used for real security.
* Fernet provides substantially stronger cryptographic protection than the educational algorithms.
* Encryption keys must be protected and should not be committed to a public repository.
* Path validation reduces path traversal risk but should not be treated as a complete security model.
* The project has not undergone a formal security audit.
* Production use would require additional hardening, testing, key-management controls, and threat-model-driven security review.

---

## Current Status

The current implementation provides:

* Modular file management
* Vault-oriented file isolation
* Byte-based file I/O
* Abstract encryption interface
* Multiple encryption strategies
* Dynamic encryption registry
* Composable encryption pipelines
* CLI interaction
* Operator overloading
* Vault comparison
* Integration and readiness tests

The architecture is intentionally extensible, allowing future features to be added without tightly coupling them to the existing file-management layer.

---

## Future Development

Possible future directions include:

* Expanded automated test coverage
* Migration to a structured `pytest` test suite
* Improved error handling and exception reporting
* More robust configuration management
* Runtime strategy configuration
* Additional modern cryptographic schemes where technically justified
* Improved key-management architecture
* GUI or alternative user interfaces
* Packaging the project as a reusable Python package

Future features are not considered part of the current implementation unless explicitly added to the codebase.

---

## Author

**Sara Mohammed Abd AL_Zahra**

**Lead Developer & Project Owner**

The project was designed, implemented, and documented as an independent software project exploring secure file handling, cryptographic abstraction, and object-oriented architecture in Python.

---

## License

This project is released under the **MIT License**.

See `LICENSE` for the full license text.
