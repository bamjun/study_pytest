import pytest
import my_functions  # conftest.py


def test_add():
    result = my_functions.add(number_one=1, number_two=2)
    assert result == 4
#shell

# $ pytest tests/test_03.py
# ====================================================== test session starts =======================================================
# platform win32 -- Python 3.12.1, pytest-8.1.0, pluggy-1.4.0
# rootdir: C:\Projects\practice_django\20240304-pytest
# collected 1 item                                                                                                                   

# tests\test_03.py F                                                                                                          [100%]

# ============================================================ FAILURES ============================================================ 
# ____________________________________________________________ test_add ____________________________________________________________ 

#     def test_add():
#         result = my_functions.add(number_one=1, number_two=2)
# >       assert result == 4
# E       assert 3 == 4

# tests\test_03.py:7: AssertionError
# ==================================================== short test summary info ===================================================== 
# FAILED tests/test_03.py::test_add - assert 3 == 4
# ======================================================= 1 failed in 0.33s ======================================================== 