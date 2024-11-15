import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from triangle import area, perimeter

def test_area_valid_triangle():
    a, b, c = 3, 4, 5
    expected_area = 6.0
    result = area(a, b, c)
    assert result == expected_area, f"Expected {expected_area}, but got {result}"

def test_area_zero_side():
    a, b, c = 0, 4, 5
    with pytest.raises(ValueError):
        area(a, b, c)

def test_area_negative_side():
    a, b, c = -3, 4, 5
    with pytest.raises(ValueError):
        area(a, b, c)
def test_area_invalid_triangle():
    a, b, c = 1, 2, 10
    with pytest.raises(ValueError):
        area(a, b, c)


def test_perimeter_valid_triangle():
    a, b, c = 3, 4, 5
    expected_perimeter = a + b + c
    result = perimeter(a, b, c)
    assert result == expected_perimeter, f"Expected {expected_perimeter}, but got {result}"

def test_perimeter_zero_side():
    a, b, c = 0, 4, 5
    with pytest.raises(ValueError):
        perimeter(a, b, c)

def test_perimeter_negative_side():
    a, b, c = -3, 4, 5
    with pytest.raises(ValueError):
        perimeter(a, b, c)