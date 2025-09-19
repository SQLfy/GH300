import math
from aplusb import add

# File: /D:/Repo/GH300/test_aplusb.py
# Updated to avoid requiring the pytest package for static analyzers;
# uses math.isclose for approximate equality checks.

def test_add_integers():
    assert add(1, 2) == 3

def test_add_floats():
    assert math.isclose(add(0.1, 0.2), 0.3, rel_tol=1e-9, abs_tol=0.0)

def test_add_negative_and_positive():
    assert math.isclose(add(-1.5, 2.5), 1.0, rel_tol=1e-9, abs_tol=0.0)

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5

def test_add_large_numbers():
    assert math.isclose(add(1e18, 1e18), 2e18, rel_tol=1e-12, abs_tol=0.0)

def test_add_nan():
    result = add(float('nan'), 1.0)
    assert math.isnan(result)

def test_add_infinity():
    assert math.isinf(add(float('inf'), 1.0))
    assert math.isinf(add(float('-inf'), -1.0))