import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from square import area, perimeter


def test_area_positive_side():
    side = 69
    expected = side * side
    result = area(side)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_area_zero_side():
    side = 0
    expected = 0
    result = area(side)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_area_negative_side():
    side = -69
    with pytest.raises(ValueError):
        area(side)


def test_perimeter_positive_side():
    side = 69
    expected = 4 * side
    result = perimeter(side)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_perimeter_zero_side():
    side = 0
    expected = 0
    result = perimeter(side)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_perimeter_negative_side():
    side = -69
    with pytest.raises(ValueError):
        perimeter(side)
