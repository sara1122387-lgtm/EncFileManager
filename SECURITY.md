# Security Policy

## Overview

EncFileManager is an educational and architectural Python project focused on secure file handling, encryption abstraction, and object-oriented design.

Although the project includes security-oriented mechanisms such as controlled vault paths and authenticated encryption through Fernet, it has not undergone a formal security audit and should not be considered a production-grade security system.

## Supported Security Concerns

Security reports are relevant to issues such as:

* Path traversal or unintended access outside the configured vault.
* Incorrect enforcement of vault path boundaries.
* Unexpected exposure of plaintext data.
* Incorrect encryption or decryption behavior.
* Insecure handling of encryption keys introduced by the project itself.
* Vulnerabilities that allow unauthorized file access or manipulation.

## Out of Scope

The following are generally outside the scope of this project:

* Vulnerabilities in Python or third-party dependencies that have not been introduced by EncFileManager.
* Issues requiring physical access to the user's machine.
* Security limitations inherent to intentionally educational algorithms such as Caesar and XOR.
* Features or attack scenarios outside the current implementation.

## Encryption Notice

Caesar and XOR are included for educational purposes and are not considered secure cryptographic algorithms.

Fernet is the project's practical authenticated encryption option. However, secure deployment also depends on proper key management.

Encryption keys must not be committed to the public repository.

## Reporting a Security Issue

If you identify a potential security issue, please avoid publicly disclosing sensitive details before the issue can be reviewed.

For non-sensitive issues, GitHub Issues may be used for discussion.

For potentially sensitive vulnerabilities, please contact the repository owner privately through an appropriate GitHub communication channel.

When reporting an issue, please provide:

* A clear description of the vulnerability.
* The affected component or file.
* Steps required to reproduce the behavior.
* The expected behavior.
* The observed behavior.
* Any relevant security impact.

## Security Development

Security-related improvements may include:

* Expanded automated testing.
* Stronger path validation.
* Improved exception handling.
* More robust key-management practices.
* Dependency updates.
* Additional security-focused test cases.
* Threat-model-driven hardening.

Security claims in this project are intentionally limited to the behavior implemented and tested by the current codebase.
