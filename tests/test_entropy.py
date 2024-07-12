import pytest
import math
from src.entropy_checker import find_pool, entropy_test


def test_find_pool():
    # 26 (upper) + 26 (lower) + 10 (digits) + 32 (special)
    assert find_pool("StrongPass123!") == 94
    assert find_pool("weakpass") == 26  # 26 (lower)
    # 26 (upper) + 26 (lower) + 10 (digits)
    assert find_pool("NoSpecial123") == 62
    # 26 (upper) + 10 (digits) + 32 (special)
    assert find_pool("NOLOWERCASE123!") == 68
    # 26 (lower) + 10 (digits) + 32 (special)
    assert find_pool("nouppercase123!") == 68
    # 26 (upper) + 26 (lower) + 32 (special)
    assert find_pool("NoNumbers!!") == 84
    # 26 (upper) + 26 (lower) + 10 (digits) + 32 (special)
    assert find_pool("Short1!") == 94


def test_entropy_test():
    pool_size = find_pool("StrongPass123!")
    entropy = entropy_test(pool_size, "StrongPass123!")
    assert math.isclose(entropy, 91.76, rel_tol=1e-2)

    pool_size = find_pool("weakpass")
    entropy = entropy_test(pool_size, "weakpass")
    assert math.isclose(entropy, 37.60, rel_tol=1e-2)

    pool_size = find_pool("NoSpecial123")
    entropy = entropy_test(pool_size, "NoSpecial123")
    assert math.isclose(entropy, 71.45, rel_tol=1e-2)

    pool_size = find_pool("NOLOWERCASE123!")
    entropy = entropy_test(pool_size, "NOLOWERCASE123!")
    assert math.isclose(entropy, 91.31, rel_tol=1e-2)

    pool_size = find_pool("nouppercase123!")
    entropy = entropy_test(pool_size, "nouppercase123!")
    assert math.isclose(entropy, 91.31, rel_tol=1e-2)

    pool_size = find_pool("NoNumbers!!")
    entropy = entropy_test(pool_size, "NoNumbers!!")
    assert math.isclose(entropy, 70.32, rel_tol=1e-2)  # Corrected expectation

    pool_size = find_pool("Short1!")
    entropy = entropy_test(pool_size, "Short1!")
    assert math.isclose(entropy, 45.88, rel_tol=1e-2)  # Corrected expectation


if __name__ == "__main__":
    pytest.main()
