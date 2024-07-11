import unittest
import re
from pathlib import Path
from strength import strength_len_char, check_comm
from _regex_patterns import LEAST_LENGTH, UPPERCASE, LOWERCASE, DIGITS, SPECIAL


class TestStrength(unittest.TestCase):

    def test_strength_len_char(self):
        # Test case: all character types present
        password = "StrongPass123!"
        result = strength_len_char(password)
        self.assertTrue(result, "Password should be considered strong.")

        # Test case: too short
        password = "Short1!"
        result = strength_len_char(password)
        self.assertFalse(result, "Password should be considered too short.")

        # Test case: no uppercase letters
        password = "strongpass123!"
        result = strength_len_char(password)
        self.assertFalse(
            result, "Password should be considered weak due to no uppercase letters.")

        # Test case: no lowercase letters
        password = "STRONGPASS123!"
        result = strength_len_char(password)
        self.assertFalse(
            result, "Password should be considered weak due to no lowercase letters.")

        # Test case: no digits
        password = "StrongPass!"
        result = strength_len_char(password)
        self.assertFalse(
            result, "Password should be considered weak due to no digits.")

        # Test case: no special characters
        password = "StrongPass123"
        result = strength_len_char(password)
        self.assertFalse(
            result, "Password should be considered weak due to no special characters.")

    def test_check_comm(self):
        # Create a temporary common passwords file
        common_passwords_content = """
        password
        123456
        123456789
        qwerty
        abc123
        """.strip()

        common_passwords_path = Path(__file__).parent / "common_passwords.txt"
        with open(common_passwords_path, "w") as file:
            file.write(common_passwords_content)

        # Test case: common password
        password = "password"
        result = check_comm(password)
        self.assertFalse(result, "Password should be considered common.")

        # Test case: uncommon password
        password = "StrongPass123!"
        result = check_comm(password)
        self.assertTrue(result, "Password should be considered uncommon.")

        # Clean up the temporary file
        common_passwords_path.unlink()


if __name__ == '__main__':
    unittest.main()
