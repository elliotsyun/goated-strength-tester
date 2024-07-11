"""
This module provides functions that test the strength of a password based on criteria such as length, use of special characters, and common password checks.

Functions:
    check_length_char(password): Checks the length of the password to ensure it is at least 11 symbols and verifies the use of uppercase letters, lowercase letters, numbers, and special characters (!, @, #, $, %, ^, &, *).
    check_comm(password): Checks that the password is not a commonly used password by comparing it against a list in 'common_passwords.txt'.

Examples:
    To check if a password meets the required strength criteria:

    >>> is_strong = check_length_char("StrongPass123!")
    >>> print(is_strong)

    To verify that a password is not a commonly used one:

    >>> is_unique = check_comm("password123")
    >>> print(is_unique)

Author:
    Elliot Yun

Date:
    2024-07-11

Version:
    1.0.2
"""

import re
from pathlib import Path
from _regex_patterns import LEAST_LENGTH, UPPERCASE, LOWERCASE, DIGITS, SPECIAL


current_path = Path(__file__).parent
file_path = current_path / ".." / "docs" / "common_passwords.txt"


def strength_len_char(password):
    """
    Checks the strength of a password based on its length and character composition.

    This function verifies that the password:
    - Has no spaces.
    - Is at least 11 characters long.
    - Contains at least one uppercase letter, one lowercase letter, one number, and one special character (!, @, #, $, %, ^, &, *).

    Parameters:
        password (str): The password to be checked.

    Returns:
        bool: True if the password meets all the requirements, False otherwise.
    """
    is_valid = True
    no_space = password.strip()
    errors = []

    checks = [
        (lambda password: ' ' not in password,
         "Please do not put spaces in your password."),
        (lambda password: len(password) < LEAST_LENGTH,
         "Your password is under the required safe length (11)."),
        (lambda password: re.search(UPPERCASE, password),
         "Your password must contain at least one capital letter.")
        (lambda password: re.search(LOWERCASE, password),
         "Your password must contain at least one lowercase letter.")
        (lambda password: re.search(DIGITS, password),
         "Your password must contain at least one number.")
        (lambda password: re.search(SPECIAL, password),
         "Your password must contain at least one special character.")
    ]

    # store message in lambdafunc, message thats in the checks list
    # if the lambdafunc is not true

    errors = [message for lambdafunc,
              message in checks if not lambdafunc(password)]

    if errors:
        for error in errors:
            print(error)
        print("Your password does not meet all the requirements.")
        return False
    else:
        print("Your password meets all the requirements.")
        return True


def check_comm(password):
    """
    Checks if the password is a commonly used password.

    This function compares the provided password against a list of common passwords stored in 'common_passwords.txt'.

    Parameters:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is not a commonly used password, False if it is.
    """
    with open(file_path, "r") as file:
        for line in file:
            if password.strip() == line.strip():
                print("Password is a common password, please choose another password.")
                return False
    return True
