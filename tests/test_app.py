# tests/test_app.py

import pytest
from calculator import add_numbers  # Importing the add_numbers function

# Test Case 1: Add two positive numbers
def test_add_positive_numbers():
    """Test adding two positive numbers."""
    print("Test Case 1: Adding two positive numbers")
    assert add_numbers(2, 3) == 5

# Test Case 2: Add two negative numbers
def test_add_negative_numbers():
    """Test adding two negative numbers."""
    print("Test Case 2: Adding two negative numbers")
    assert add_numbers(-2, -3) == -5

# Test Case 3: Add a negative number and a positive number
def test_add_mixed_numbers():
    """Test adding a negative number and a positive number."""
    print("Test Case 3: Adding a negative number and a positive number")
    assert add_numbers(-2, 3) == 1

# Test Case 4: Add zero to a number
def test_add_with_zero():
    """Test adding zero to a number."""
    print("Test Case 4: Adding zero to a number")
    assert add_numbers(0, 5) == 5

# Test Case 5: Add two floating-point numbers
def test_add_floats():
    """Test adding two floating-point numbers."""
    print("Test Case 5: Adding two floating-point numbers")
    assert add_numbers(2.5, 3.5) == 6.0

# Test Case 6: Add large numbers
def test_add_large_numbers():
    """Test adding large numbers."""
    print("Test Case 6: Adding large numbers")
    assert add_numbers(1000000, 2000000) == 3000000

# Test Case 7: Handle invalid input (non-numeric)
def test_add_non_numeric():
    """Test that adding non-numeric values raises a TypeError."""
    print("Test Case 7: Handling invalid input (non-numeric)")
    with pytest.raises(TypeError):
        add_numbers("2", 3)