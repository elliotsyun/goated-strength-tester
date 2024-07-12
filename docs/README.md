### Goated Strength Tester

```markdown
# Password Strength Evaluator

This repository provides functions to evaluate the strength of a password based on entropy calculations and character composition. It also includes functions to check if a password meets specific criteria and if it is a commonly used password.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Entropy Checker](#entropy-checker)
  - [Password Strength Checker](#password-strength-checker)
- [Testing](#testing)
- [Examples](#examples)
- [Author](#author)

## Installation

Clone the repository:

```bash
git clone https://github.com/elliotsyun/goated-strength-tester.git
cd password-strength-evaluator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Entropy Checker

The entropy checker evaluates the strength of a password based on entropy calculations and character composition.

#### Functions

- `find_pool(password)`: Determines the size of the character pool based on the types of characters in the password.
- `entropy_test(pool, password)`: Calculates the entropy of the password and classifies its strength.

### Password Strength Checker

The password strength checker tests the strength of a password based on criteria such as length, use of special characters, and common password checks.

#### Functions

- `strength_len_char(password)`: Checks the length of the password to ensure it is at least 11 symbols and verifies the use of uppercase letters, lowercase letters, numbers, and special characters.
- `check_comm(password)`: Checks that the password is not a commonly used password by comparing it against a list in 'common_passwords.txt'.

## Testing

Unit tests are provided for the functions using `pytest`. To run the tests, navigate to the root directory of the project and execute:

```bash
pytest tests
```

## Examples

### Entropy Checker

To determine the character pool size of a password:

```python
from src.entropy_checker import find_pool

pool_size = find_pool("StrongPass123!")
print(pool_size)
```

To calculate the entropy of a password and classify its strength:

```python
from src.entropy_checker import entropy_test

pool_size = find_pool("StrongPass123!")
entropy = entropy_test(pool_size, "StrongPass123!")
print(entropy)
```

### Password Strength Checker

To check if a password meets the required strength criteria:

```python
from src.pass_strength import strength_len_char

is_strong = strength_len_char("StrongPass123!")
print(is_strong)
```

To verify that a password is not a commonly used one:

```python
from src.pass_strength import check_comm

is_unique = check_comm("password123")
print(is_unique)
```

## Author

Elliot Yun

**Date**: 2024-07-12

**Version**: 1.0.3
