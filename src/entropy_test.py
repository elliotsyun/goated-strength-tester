import re
from _regex_patterns import LEAST_LENGTH, UPPERCASE, LOWERCASE, NUMBER, SPECIAL

# entropy calculation: E = log2(R^L), R = size of pool of unique char, L = pass length

def entropy_test(password):
    # determine the length of the password

    length = len(password)
    pool = 0

    # if it contains a certain character, add specified num to pool

    if 

