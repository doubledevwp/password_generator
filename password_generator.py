#!/usr/bin/env python3

import sys
import random

def password_generator(num, special_char = False):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    special = ',.<>/?;:[{}]\|!@#$%^&*()_+-=*'
    password = ''

    if special_char:
        char += special

    for l in range(num):
        password += random.choice(char)

    print(password)

if __name__ == '__main__':
    arguments = len(sys.argv)

    if arguments > 1:
        number_of_characters = int(sys.argv[1]) if sys.argv[1].isdigit() else exit("\n\tINVALID ENTRY!\n\n\tPlease enter a number\n\tfor you password length.\n")
        add_special_characters = True if len(sys.argv) > 2 and sys.argv[2] == 'True' else None
    else:
        exit("\n\tNo arguments passed in.\n\n\tPlease pass in at least\n\tthe length of the password\n\tyou are trying to create.\n")

    password_generator(number_of_characters, add_special_characters)
