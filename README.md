# password_generator
Simple password generator

This script takes two required inputs.

The first required flag is the length; `=l`.  N is going to be the length of the password you are going to create.
The second required flag is one of the following:
| Flag | Description |
| --- | --- |
| -d | Include digits |
| -lc | Include lower case characters |
| -uc | Include upper case characters |
| -s | Include special characters |

password_generator.py -l N -{d|lc|uc|s}

## EXAMPLES
Password length of 10 and only special characters:
1. password_generator.py -l 10 -s
1. password_generator.py -l 10 True

Password length of 14 and only lower case characters:
1. password_generator.py -l 10 -lc
1. password_generator.py -l 10 False True

Password length of 50 and lower case and upper case characters:
1. password_generator.py -l 50 -lc -uc
1. password_generator.py -l 50 False True True
