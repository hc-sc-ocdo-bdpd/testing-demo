import sys, os
import pytest
sys.path.append(os.path.join(sys.path[0],'src'))
from src.functions import add


def test_add():
    assert add(1,1) == 2
    assert add(1,2) == 3




variable_names = "a, b, c"
values = [(1, 1, 2), 
          (4, 5, 9)]

@pytest.mark.parametrize(variable_names, values)
def test_parameterized(a, b, c):
    assert add(a,b) == c


