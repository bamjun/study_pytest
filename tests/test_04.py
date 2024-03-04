import pytest
import my_functions  # conftest.py


def test_add():
    result = my_functions.add(number_one=1, number_two=2)
    assert result == 3

def test_divide():
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2

#shell

# $ pytest tests/test_04.py