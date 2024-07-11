import re
import math
from _regex_patterns import UPPERCASE, LOWERCASE, DIGITS, SPECIAL


def find_pool(password):
    # determine the length of the password
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
