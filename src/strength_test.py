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
    2024-06-25

Version:
    1.0.0
"""

import re
from pathlib import Path

LEAST_LENGTH = 11
UPPERCASE_PATTERN = r"[A-Z]"
LOWERCASE_PATTERN = r"[a-z]"
NUMBER_PATTERN = r"\d"
SPECIAL_CHAR_PATTERN = r"[!@#$%^&*]"

current_path = Path(__file__).parent
file_path = current_path / ".." / "docs" / "common_passwords.txt"


def check_length_char(password):
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

    if len(password) != len(no_space):
        print("Please do not put spaces in your password.")
        is_valid = False

    if len(password) < LEAST_LENGTH:
        print("Your password is under the required safe length (11).")
        is_valid = False

    if (
        not re.search(UPPERCASE_PATTERN, password)
        or not re.search(LOWERCASE_PATTERN, password)
        or not re.search(NUMBER_PATTERN, password)
        or not re.search(SPECIAL_CHAR_PATTERN, password)
    ):
        print(
            "Your password does not have enough uses of capital letters, lowercase letters, numbers, or symbols (!, @, #, $, %, ^, &, *)."
        )
        is_valid = False

    if is_valid:
        print("Your password meets all the requirements.")
        return True

    else:
        print("Your password does not meet all the requirements")
        return False


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
