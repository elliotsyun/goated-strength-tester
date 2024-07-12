import pytest
from pathlib import Path
from src.pass_strength import strength_len_char, check_comm

# Mock data and constants
common_passwords_path = Path(__file__).parent / \
    ".." / "docs" / "common_passwords.txt"


@pytest.fixture
def setup_common_passwords():
    # Setup common passwords for testing
    passwords = ["password123", "123456", "qwerty", "abc123", "password"]
    with open(common_passwords_path, "w") as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    yield
    # Teardown if needed


def test_strength_len_char():
    assert strength_len_char("StrongPass123!") is True
    assert strength_len_char("weakpass") is False
    assert strength_len_char("NoSpecial123") is False
    assert strength_len_char("nouppercase123!") is False
    assert strength_len_char("NOLOWERCASE123!") is False
    assert strength_len_char("NoNumbers!!") is False
    assert strength_len_char("Short1!") is False


def test_check_comm(setup_common_passwords):
    assert check_comm("StrongPass123!") is True
    assert check_comm("password123") is False
    assert check_comm("qwerty") is False
    assert check_comm("uniquePass123!") is True


if __name__ == "__main__":
    pytest.main()
