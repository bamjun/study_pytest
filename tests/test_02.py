import pytest
import my_functions  # conftest.py

def test_add():
    result = my_functions.add(number_one=1, number_two=2)
    assert result == 3

#shell

# $ pytest tests/test_02.py
# ====================================================== test session starts =======================================================
# platform win32 -- Python 3.12.1, pytest-8.1.0, pluggy-1.4.0
# rootdir: C:\Projects\practice_django\20240304-pytest
# collected 1 item

# tests\test_02.py .                                                                                                          [100%] 

# ======================================================= 1 passed in 0.02s ======================================================== 