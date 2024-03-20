import pytest

from main import factorial

def test_factorial_with_positive_integer():
    assert factorial(5) == 120

def test_factorial_with_zero():
    assert factorial(0) == 1

def test_factorial_with_negative_integer():
    with pytest.raises(ValueError):
        factorial(-5)

def test_factorial_with_large_number():
    assert factorial(10) == 3628800

def test_factorial_with_one():
    assert factorial(1) == 1

def test_factorial_with_float():
    with pytest.raises(TypeError):
        factorial(5.5)

def test_factorial_with_string():
    with pytest.raises(TypeError):
        factorial("5")

def test_factorial_with_list():
    with pytest.raises(TypeError):
        factorial([5])
