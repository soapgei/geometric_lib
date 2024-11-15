import sys
import os
from math import pi
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from calculate import calc


def test_calc_valid_circle_area():
    fig = 'circle'
    func = 'area'
    size = [5]
    expected = pi*size[0]*size[0]
    result = calc(fig, func, size)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_calc_valid_circle_perimeter():
    fig = 'circle'
    func = 'perimeter'
    size = [5]
    expected_result =2*pi*size[0]
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_calc_valid_square_area():
    fig = 'square'
    func = 'area'
    size = [4]
    expected_result = size[0]*size[0]
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected {expected}, but got {result}"

def test_calc_valid_square_perimeter():
    fig = 'square'
    func = 'perimeter'
    size = [4]
    expected = size[0]*size[0]
    result = calc(fig, func, size)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_calc_valid_triangle_area():
    fig = 'triangle'
    func = 'area'
    size = [3, 4, 5]
    expected_result = 6.0
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_calc_valid_triangle_perimeter():
    fig = 'triangle'
    func = 'perimeter'
    size = [3, 4, 5]
    expected_result = sum(size)
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_calc_invalid_figure():
    fig = 'hexagon'
    func = 'area'
    size = [6]
    with pytest.raises(ValueError, match="Invalid figure"):
        calc(fig, func, size)

def test_calc_invalid_func():
    fig = 'circle'
    func = 'volume'
    size = [5]
    with pytest.raises(ValueError):
        calc(fig, func, size)


def test_calc_neg_size():
    fig = 'circle'
    func = 'area'
    size = [-5]
    with pytest.raises(ValueError):
        calc(fig, func, size)

def test_calc_invalid_size_count_triangle():
    fig = 'triangle'
    func = 'perimeter'
    size = [3, 4]
    with pytest.raises(ValueError):
        calc(fig, func, size)

def test_calc_incorrect_size_count_circle():
    fig = 'circle'
    func = 'area'
    size = [5, 10]
    with pytest.raises(ValueError):
        calc(fig, func, size)

def test_calc_invalid_triangle():
    fig = 'triangle'
    func = 'area'
    size = [1, 2, 10]
    with pytest.raises(ValueError):
        calc(fig, func, size)
