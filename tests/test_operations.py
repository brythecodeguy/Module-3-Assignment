import pytest
from app.operations import add, subtract, multiply, divide


def test_add():
    assert add(2.0, 3.0) == 5.0


def test_add_negative():
    assert add(-2.0, -3.0) == -5.0


def test_subtract():
    assert subtract(5.0, 2.0) == 3.0


def test_subtract_negative():
    assert subtract(2.0, 5.0) == -3.0


def test_multiply():
    assert multiply(4.0, 5.0) == 20.0


def test_multiply_negative():
    assert multiply(-4.0, 5.0) == -20.0


def test_divide():
    assert divide(10.0, 2.0) == 5.0


def test_divide_negative():
    assert divide(-10.0, 2.0) == -5.0


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide(1.0, 0.0)