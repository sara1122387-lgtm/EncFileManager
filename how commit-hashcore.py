# [33mcommit d4b905141f02e4936a77f016d8707896f76b9e64[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m)[m
# Author: sara_mohammed <sara1122387@gmail.com>
# Date:   Fri Oct 31 08:32:19 2025 +0300
#
#     Refactor core.py for safer file handling
#     >
#     > - Replace os.path with pathlib.Path for all file operations
#     > - Fix read() and rename() path issues in FileHandler
#     > - Improve file extension validation
#     > - Ensure EncFileManager only accesses files within vault
#
# [33mcommit a4d7b0a2f7e707eedf8d268ee01bfd899419b1aa[m
# Author: sara_mohammed <sara1122387@gmail.com>
# Date:   Fri Oct 24 01:59:04 2025 +0300
#
#     Initial release of EncFileManager
