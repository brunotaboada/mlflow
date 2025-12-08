# Coding Standards

## Language

All source code must be written in English, including variable names, functions, classes, comments, and documentation.

**Example:**
```python
# ❌ Avoid
nome_do_produto = "Laptop"
def calcular_preco():
    pass

# ✅ Prefer
product_name = "Laptop"
def calculate_price():
    pass
```

## Naming Conventions

### snake_case
Use for variables, functions, and methods.

**Example:**
```python
user_name = "John"
is_active = True

def get_user_by_id(user_id: str):
    pass
```

### PascalCase
Use for classes.

**Example:**
```python
class UserRepository:
    pass

class PaymentGateway:
    pass
```

### kebab-case
Use for files and directories.

**Example:**
```
user-repository.py
payment-gateway-service.py
api-controllers/
```

## Clear Naming

Avoid abbreviations, but also don't write overly long names (more than 30 characters).

**Example:**
```python
# ❌ Avoid
usr_nm = "John"  # too abbreviated
user_name_from_database_query_result = "John"  # too long

# ✅ Prefer
user_name = "John"
db_user_name = "John"
```

## Constants and Magic Numbers

Declare constants to represent magic numbers with readability.

**Example:**
```python
# ❌ Avoid
if user.age >= 18:
    pass
time.sleep(3600)

# ✅ Prefer
MINIMUM_AGE = 18
ONE_HOUR_IN_SECONDS = 60 * 60

if user.age >= MINIMUM_AGE:
    pass
time.sleep(ONE_HOUR_IN_SECONDS)
```

## Methods and Functions

Methods and functions should perform a clear and well-defined action, and this should be reflected in their name, which should start with a verb, never a noun.

**Example:**
```python
# ❌ Avoid
def user(user_id: str):
    pass

def user_data():
    pass

# ✅ Prefer
def get_user(user_id: str):
    pass

def fetch_user_data():
    pass

def create_user(data: dict):
    pass

def update_user_email(user_id: str, email: str):
    pass
```

## Parameters

Whenever possible, avoid passing more than 3 parameters. Prefer using objects/dictionaries when necessary.

**Example:**
```python
# ❌ Avoid
def create_user(name: str, email: str, age: int, address: str, phone: str):
    pass

# ✅ Prefer
def create_user(params: dict):
    pass

# Usage:
create_user({
    "name": "John",
    "email": "john@example.com",
    "age": 30,
    "address": "123 Main St",
    "phone": "555-1234"
})
```

## Side Effects

Avoid side effects. Generally, a method or function should either mutate OR query, never allow a query to have side effects.

**Example:**
```python
# ❌ Avoid
def get_users():
    users = database.query("SELECT * FROM users")
    logger.log("Users fetched")  # side effect
    cache.set("users", users)  # side effect
    return users

# ✅ Prefer
def get_users():
    return database.query("SELECT * FROM users")

def fetch_and_cache_users():
    users = get_users()
    logger.log("Users fetched")
    cache.set("users", users)
    return users
```

## Conditional Structures

Never nest more than two if/else statements. Always prefer early returns.

**Example:**
```python
# ❌ Avoid
def process_payment(user, amount):
    if user:
        if user.is_active:
            if amount > 0:
                if user.balance >= amount:
                    return complete_payment(user, amount)
    return None

# ✅ Prefer
def process_payment(user, amount):
    if not user:
        return None
    if not user.is_active:
        return None
    if amount <= 0:
        return None
    if user.balance < amount:
        return None

    return complete_payment(user, amount)
```

## Flag Parameters

Never use flag parameters to switch the behavior of methods and functions. In these cases, extract to methods and functions with specific behaviors.

**Example:**
```python
# ❌ Avoid
def get_user(user_id: str, include_orders: bool):
    user = database.get_user(user_id)
    if include_orders:
        user.orders = database.get_orders(user_id)
    return user

# ✅ Prefer
def get_user(user_id: str):
    return database.get_user(user_id)

def get_user_with_orders(user_id: str):
    user = get_user(user_id)
    user.orders = database.get_orders(user_id)
    return user
```

## Method and Class Size

- Avoid long methods, with more than 50 lines
- Avoid long classes, with more than 300 lines

**Example:**
```python
# ❌ Avoid
class UserService:
    # 500 lines of code
    pass

# ✅ Prefer
class UserAuthService:
    pass

class UserProfileService:
    pass

class UserNotificationService:
    pass
```

## Formatting

Avoid blank lines within methods and functions.

**Example:**
```python
# ❌ Avoid
def calculate_total(items):
    subtotal = sum(item.price for item in items)

    tax = subtotal * 0.1

    return subtotal + tax

# ✅ Prefer
def calculate_total(items):
    subtotal = sum(item.price for item in items)
    tax = subtotal * 0.1
    return subtotal + tax
```

## Comments

Avoid using comments whenever possible. Code should be self-explanatory.

**Example:**
```python
# ❌ Avoid
# Check if user is adult
if user.age >= 18:
    pass

# ✅ Prefer
is_adult = user.age >= MINIMUM_LEGAL_AGE
if is_adult:
    pass
```

## Variable Declaration

Never declare more than one variable on the same line.

**Example:**
```python
# ❌ Avoid
name, age, email = "John", 30, "john@example.com"

# ✅ Prefer
name = "John"
age = 30
email = "john@example.com"
```

## Variable Scope

Declare variables as close as possible to where they will be used.

**Example:**
```python
# ❌ Avoid
def process_order(order_id: str):
    user = get_user()
    product = get_product()
    discount = calculate_discount()

    validate_order(order_id)
    check_inventory(order_id)

    # user is only used here, 5 lines later
    notify_user(user)

# ✅ Prefer
def process_order(order_id: str):
    validate_order(order_id)
    check_inventory(order_id)

    user = get_user()
    notify_user(user)
```

## Python-Specific Best Practices

### Type Hints

Use Python type hints for better code clarity and IDE support.

**Example:**
```python
# ✅ Recommended
def calculate_total(items: list[Item]) -> float:
    return sum(item.price for item in items)

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

### Context Managers

Use context managers for resource handling.

**Example:**
```python
# ✅ Recommended
with open('file.txt', 'r') as f:
    content = f.read()

# Instead of:
f = open('file.txt', 'r')
content = f.read()
f.close()
```

### List Comprehensions

Prefer list comprehensions over traditional loops when appropriate.

**Example:**
```python
# ✅ Recommended
squares = [x**2 for x in range(10)]

# Instead of:
squares = []
for x in range(10):
    squares.append(x**2)
```

### String Formatting

Use f-strings for string formatting (Python 3.6+).

**Example:**
```python
# ✅ Recommended
name = "John"
greeting = f"Hello, {name}!"

# Instead of:
greeting = "Hello, %s!" % name
greeting = "Hello, {}!".format(name)
```

### Exception Handling

Be specific with exception handling.

**Example:**
```python
# ✅ Recommended
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")

# Instead of:
try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")
```

### Virtual Environments

Always use virtual environments for Python projects.

**Example:**
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate
```

### Imports

Organize imports according to PEP 8 guidelines.

**Example:**
```python
# ✅ Recommended
# Standard library imports
import os
import sys

# Third-party imports
import numpy as np
import pandas as pd

# Local application imports
from .models import User
from .utils import helpers
```

### Docstrings

Use docstrings to document modules, classes, and functions.

**Example:**
```python
def calculate_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle
        height: The height of the rectangle

    Returns:
        The calculated area
    """
    return width * height
```

### Testing

Write unit tests for your code using pytest or unittest.

**Example:**
```python
# test_calculator.py
import pytest
from calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

### Performance Considerations

Use built-in functions and libraries when possible for better performance.

**Example:**
```python
# ✅ Recommended - Use built-in sum()
total = sum(numbers)

# Instead of manual implementation
total = 0
for num in numbers:
    total += num
```

### Logging

Use the logging module instead of print statements for debugging.

**Example:**
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Recommended
logger.info("Processing started")
logger.debug("Debug information: %s", some_variable)
logger.error("An error occurred: %s", error_message)
```

### Environment Variables

Use environment variables for configuration.

**Example:**
```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
```

### Dependency Management

Use requirements.txt or pyproject.toml for dependency management.

**Example requirements.txt:**
```
requests==2.28.1
numpy>=1.21.0
pandas==1.4.2
```

### Code Formatting

Use tools like black, isort, and flake8 for consistent code formatting.

**Example .pre-commit-config.yaml:**
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
```

### Version Control

Follow good Git practices:
- Write meaningful commit messages
- Use feature branches
- Keep commits small and focused
- Write good pull request descriptions

### Documentation

Maintain good documentation:
- Keep README.md up to date
- Document installation and usage
- Include examples
- Document API endpoints if applicable