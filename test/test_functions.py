import sys, os
import pytest
sys.path.append(os.path.join(sys.path[0],'src'))
from src.functions import add

variable_names = "a, b, c"
values = [(1, 1, 2), 
          (4, 5, 9)]

@pytest.mark.parametrize(variable_names, values)
def test_parameterized(a, b, c):
    assert add(a,b) == c


'''
def test_add():
    assert add(1,1) == 2
    assert add(1,2) == 3


@pytest.fixture
def input_value():
   # Setup
   input = 39
   yield input
   # Tear down

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0


def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
'''
