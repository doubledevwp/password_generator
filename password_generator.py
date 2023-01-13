#!/usr/bin/env python3

import random # For random.choice()
import string # For digits, lower|uppercase, and special characters
import argparse # For help functionality when calling this file in the CLI
from utilities import try_parse_int # Custom utility file for try_parse_int()

# Generate password
# Returns generated password or None
def password_generator(num = None,
                       use_digit_chars = False,
                       use_lower_chars = False,
                       use_upper_chars = False,
                       use_special_chars = False):

    # Validating there was a number passed in from the external import call
    if not num:
        print('No length was specified when calling password_generator')
        return

    # Setting variables
    chars = ''
    password = ''

    # Checking the flags
    if use_digit_chars:
        chars += string.digits

    if use_lower_chars:
        chars += string.ascii_lowercase

    if use_special_chars:
        chars += string.punctuation

    if use_upper_chars:
        chars += string.ascii_uppercase

    # Validating there are characters to choose from external import call
    if not chars:
        print('No flags were set when calling password_generator')
        return

    # Generating password
    for i in range(num):
        password += random.choice(chars)

    # Returning password
    return password

# Main entry point of program
if __name__ == '__main__':
    # Command line argument parser
    parser = argparse.ArgumentParser(
                        prog='password_generator.py',
                        description='Program to generate random passwords with the ability to customize length, which alphanumeric and special characters to use',
                        
                        epilog='And now eat your damn cake!')
    parser.add_argument('-l', help='Length of password generated [REQUIRED]', required=True)
    parser.add_argument('-d', action='store_true', help='Add flag to inclue digits')
    parser.add_argument('-lc', action='store_true', help='Add flag to include lowercase letters')
    parser.add_argument('-uc', action='store_true', help='Add flag to include uppercase letters')
    parser.add_argument('-s', action='store_true', help='Add flag to include special charaters')

    # Parse the arguments
    args = parser.parse_args()

    # Convert password length argument to int
    length = try_parse_int(args.l)

    # Validating that length is a number from the try_parse_int() above
    if not length:
        exit('\n\tNo length specified or input can\'t be converted to an number!\n\tPlease refer back to the documentation:\n\n\t$ python password_generator.py -h\n')

    # Checking for flags
    use_digits = True if args.d else False
    use_lowers = True if args.lc else False
    use_uppers = True if args.uc else False
    use_specials = True if args.s else False

    # Validating at least one flag is set to generate a password
    if not(use_digits or use_lowers or use_specials or use_uppers):
        exit('\n\tNo flags were set resulting in no password created!\n\tPlease refer to the documentation:\n\n\t$ python password_generator.py -h\n')

    # Call password generator function
    password = password_generator(length, use_digits, use_lowers, use_uppers, use_specials)

    # Put here for testing
    # TODO: Remove when completed
    print(password)
