# These lines ensure that utils.py can be imported from a sibling folder
import sys
import numpy as np
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))

# Import functions from utils.py
from utils import add, is_even, to_uppercase, get_list_average


def test_add():
    assert add(1, 1) == 2
    assert add("1", "2") == "12"
    assert add("one", "two") == "onetwo"
    assert add(1.5, 1) == 2.5
    assert add(1, "2") == None
    # Add extra test cases here


def test_is_even():
    is_even(3) is True  # This test is incorrect; why doesn't it fail?
    assert is_even(3) == False
    assert is_even(2) == True
    assert is_even(1.5) == "your number is a decimal"
    assert is_even("2") == None
    # Add extra test cases here


def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase(1) == None
    assert to_uppercase(True) == None
    assert to_uppercase("aLluPpER") == "ALLUPPER"
    # Add extra test cases here


def test_get_list_average():
    assert get_list_average([1, 2, 3]) == 2.0
    assert get_list_average(1) == None
    assert get_list_average("string") == None
    assert get_list_average(False) == None
    assert get_list_average([2, 2, 4, 5, 5]) == 3.6
    assert np.isclose(get_list_average([1.5, 4.7, 0.7]), 2.3)
    # Add extra test cases here
