"""
This module provides functions that test the strength of a password based on criteria such as length, use of special characters, and common password checks.

Functions:
    check_length_char(): checks the length of the password to see if it is at least 11 symbols and the use of special characters in the password
    check_comm(): checks that common passwords are not used

Example:
    To encrypt a password:

    >>> result = encrypt("my_password")
    >>> print(result)

    To decrypt a password:

    >>> original = decrypt(result)
    >>> print(original)

Author:
    Elliot Yun

Date:
    2024-06-18

Version:
    1.0.1
"""

import random
import re

LEAST_LENGTH = 11
PATTERN = r"[A-Za-z0-9!@#$%^&*]+"


def check_length_char(password):
    is_valid = True

    no_space = password.strip()
    matches = re.findall(PATTERN, password)

    if len(password) != len(no_space):
        print("Please do not put spaces in your password.")
        is_valid = False

    if len(str(password)) < LEAST_LENGTH:
        print("Your password is under the required safe length (11).")
        is_valid = False

    if not matches:
        print(
            "Your password does not have enough uses of capital letters, lowercase letters, numbers, or symbols (!, @, #, $, %, ^, &, *)."
        )
        is_valid = False

    if is_valid:
        print("Your password meets all the requirements.")
        
def check_comm(password):
    
