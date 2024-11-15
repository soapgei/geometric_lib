import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import math
from circle import area, perimeter


def test_area_pos_radius():
    radius = 7
    expected = math.pi * radius * radius
    result = area(radius)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_area_zero_radius():
    radius = 0
    expected = 0
    result = area(radius)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_area_neg_radius():
    radius = -7
    with pytest.raises(ValueError):
        area(radius)


def test_perimeter_pos_radius():
    radius = 5
    expected_perimeter = 2 * math.pi * radius
    result = perimeter(radius)
    assert result == expected_perimeter, f"Expected {expected_perimeter}, but got {result}"


def test_perimeter_zero_radius():
    radius = 0
    expected_perimeter = 0
    result = perimeter(radius)
    assert result == expected_perimeter, f"Expected {expected_perimeter}, but got {result}"


def test_perimeter_negative_radius():
    radius = -5
    with pytest.raises(ValueError):
        perimeter(radius)
