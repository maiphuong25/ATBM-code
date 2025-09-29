import pytest
from calculator import add, divide

# Test cho hàm add
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -4) == -5

def test_add_mixed_numbers():
    assert add(-1, 4) == 3

# Test cho hàm divide
def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-9, 3) == -3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

