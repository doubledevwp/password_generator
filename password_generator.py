#!/usr/bin/env python3

import sys
import random
import string
import argparse

def password_generator(num, use_upper_chars = True, use_lower_chars = True, use_digit_chars = True, use_special_chars = False):
    chars = ''
    password = ''
    digit_chars = string.digits
    lower_chars = string.ascii_lowercase
    special_chars = string.punctuation
    upper_chars = string.ascii_uppercase

    if use_digit_chars:
        chars += digit_chars

    if use_lower_chars:
        chars += lower_chars
    
    if use_special_chars:
        chars += special_chars

    if use_upper_chars:
        chars += upper_chars

    for i in range(num):
        password += random.choice(chars)

    print(password)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-len", "--length", type=int)
    parser.add_argument("-d", "--digits", type=str)
    parser.add_argument("-l", "--lowercase", type=str)
    parser.add_argument("-u", "--uppercase", type=str)
    parser.add_argument("-s", "--specialchars", type=str)

    args = parser.parse_args()

    # if args.length:
    #     length = args.length
    length = args.length if isinstance(args.length, type(None)) or args.length < 1 else 0
    if not isinstance(length, int):
        exit("\n\tNo length specified!\n\tPlease refer back to the documentation:\n\n\t$ python password_generator.py -h\n")

    use_digits = True if str(args.digits).lower() in ["true", "none"] else False
    use_lowers = True if str(args.lowercase).lower() in ["true", "none"] else False
    use_uppers = True if str(args.uppercase).lower() in ["true", "none"] else False
    use_specials = True if str(args.specialchars).lower() in ["true", "none"] else False
    

    # if arguments > 1:
    #     number_of_characters = int(sys.argv[1]) if sys.argv[1].isdigit() else exit("\n\tINVALID ENTRY!\n\n\tPlease enter a number\n\tfor you password length.\n")
    #     add_special_characters = True if len(sys.argv) > 2 and sys.argv[2] == 'True' else None
    # else:
    #     exit("\n\tNo arguments passed in.\n\n\tPlease pass in at least\n\tthe length of the password\n\tyou are trying to create.\n")

    # password_generator(number_of_characters, add_special_characters)
