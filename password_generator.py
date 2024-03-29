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

    # Checking the flags
    chars = chars.join(string.digits) if use_digit_chars else chars
    chars = chars.join(string.ascii_lowercase) if use_lower_chars else chars
    chars = chars.join(string.punctuation) if use_special_chars else chars
    chars = chars.join(string.ascii_uppercase) if use_upper_chars else chars

    # Validating there are characters to choose from external import call
    if not chars:
        print('No flags were set when calling password_generator')
        return

    # Returning password
    return ''.join(random.choices(chars, k = num))

# Main entry point of program
if __name__ == '__main__':
    # Command line argument parser
    parser = argparse.ArgumentParser(
                        prog='password_generator.py',
                        formatter_class=argparse.RawTextHelpFormatter,
                        description='Program to generate random passwords with the ability to customize length, which alphanumeric and special characters to use',
                        epilog='Example 1: Generate a 10 character password with only special characters\n' +
                               '1. password_generator.py -l 10 -s\n' +
                               '2. password_generator.py -l 10 True\n\n' +
                               'Example 2: Generate a 14 character password with only lowercase charcaters:\n' +
                               '1. password_generator.py -l 14 -lc\n' +
                               '2. password_generator.py -l 14 False True\n\n' +
                               'Example 3: Generate a 50 character password with both lower and upper case characters:\n'
                               '1. password_generator.py -l 50 -lc -uc\n' +
                               '2. password_generator.py -l 50 False True True\n\n' +
                               'And now eat your damn cake!')
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
