import unittest
import re
import math
from _regex_patterns import UPPERCASE, LOWERCASE, DIGITS, SPECIAL
from entropy import find_pool, entropy_test


class TestEntropy(unittest.TestCase):

    def test_find_pool(self):
        # Test case: all character types present
        password = "P@ssw0rd123"
        pool = find_pool(password)
        self.assertEqual(
            pool, 94, "Failed to calculate pool size for password with all character types.")

        # Test case: only lowercase letters
        password = "password"
        pool = find_pool(password)
        self.assertEqual(
            pool, 26, "Failed to calculate pool size for password with only lowercase letters.")

        # Test case: only uppercase letters
        password = "PASSWORD"
        pool = find_pool(password)
        self.assertEqual(
            pool, 26, "Failed to calculate pool size for password with only uppercase letters.")

        # Test case: only digits
        password = "123456"
        pool = find_pool(password)
        self.assertEqual(
            pool, 10, "Failed to calculate pool size for password with only digits.")

        # Test case: only special characters
        password = "@#$%^&*"
        pool = find_pool(password)
        self.assertEqual(
            pool, 32, "Failed to calculate pool size for password with only special characters.")

    def test_entropy_test(self):
        # Test case: high entropy password
        password = "P@ssw0rd123"
        pool = find_pool(password)
        entropy = entropy_test(pool, password)
        self.assertGreaterEqual(
            entropy, 60, "Entropy for strong password should be at least 60.")

        # Test case: low entropy password
        password = "123456"
        pool = find_pool(password)
        entropy = entropy_test(pool, password)
        self.assertLess(
            entropy, 36, "Entropy for weak password should be less than 36.")

        # Test case: medium entropy password
        password = "password"
        pool = find_pool(password)
        entropy = entropy_test(pool, password)
        self.assertTrue(
            36 <= entropy < 60, "Entropy for medium password should be between 36 and 60.")


if __name__ == '__main__':
    unittest.main()
