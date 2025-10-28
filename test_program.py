import pytest
from Program import pow, add

def test_pow():
    assert pow(1, 1) == 1
    assert pow(2, 2) == 4
    assert pow(3, 3) == 27
    assert pow(15, 2) == 225
    assert pow(2, -2) == 0.25

def test_add():
    assert add(1, 1) == 2
    assert add(1, 2) == 3
    assert add(2, 1) == 3
    assert add(2, 2) == 4
    assert add(-51, 1) == -50
    
