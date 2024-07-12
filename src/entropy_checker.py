"""
This module provides functions to evaluate the strength of a password based on entropy calculations and character composition.

Functions:
    find_pool(password): Determines the size of the character pool based on the types of characters in the password.
    entropy_test(pool, password): Calculates the entropy of the password and classifies its strength.

Examples:
    To determine the character pool size of a password:

    >>> pool_size = find_pool("StrongPass123!")
    >>> print(pool_size)

    To calculate the entropy of a password and classify its strength:

    >>> entropy = entropy_test(pool_size, "StrongPass123!")
    >>> print(entropy)

Author:
    Elliot Yun

Date:
    2024-07-11

Version:
    1.0.2
"""

import re
import math
from src._regex_patterns import UPPERCASE, LOWERCASE, DIGITS, SPECIAL


def find_pool(password):
    """
    Determines the character pool size based on the composition of the given password.

    The function analyzes the password and increments the pool size based on the presence of:
    - Uppercase letters: 26
    - Lowercase letters: 26
    - Digits: 10
    - Special characters: 32

    Parameters:
    password (str): The password to be analyzed.

    Returns:
    int: The total size of the character pool.
    """
    pool = 0

    # if it contains a certain character, add specified num to pool
    # lowercase: 26
    # uppercase: 26
    # digits: 10
    # special: 32

    if re.search(UPPERCASE, password) is not None:
        pool += 26
    if re.search(LOWERCASE, password) is not None:
        pool += 26
    if re.search(DIGITS, password) is not None:
        pool += 10
    if re.search(SPECIAL, password) is not None:
        pool += 32

    print("This is the size of the pool: ", pool)

    return pool


def entropy_test(pool, password):
    """
    Calculates the entropy of a password based on its length and character pool size.

    The function computes the entropy using the formula: E = L * log_base_2(P)
    where L is the password length and P is the size of the character pool.
    It then classifies the password strength based on the entropy value.

    Parameters:
    pool (int): The size of the character pool.
    password (str): The password to be evaluated.

    Returns:
    float: The calculated entropy of the password.
    """
    length = len(password)

    # entropy calculation: E = L * log_base_2(P), P = size of pool, L = pass length

    entropy = length * math.log(pool, 2)

    print(f"Entropy: {entropy:.2f} bits.")

    if entropy < 36:
        print("Your password is Very Weak.")
    elif 36 <= entropy < 60:
        print("Your password is Weak.")
    elif 60 <= entropy < 120:
        print("Your password is Strong.")
    else:
        print("Your password is Very Strong.")

    return entropy
