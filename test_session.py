import pytest
from session import sum_two_element




def test_add_possitive():
    assert sum_two_element(1,2) == 3
    
def test_add_zero():
    assert sum_two_element(1,0) == 2
    
def test_add_negative():
    assert sum_two_element(4,-100)  == -96
    
    
def test_add_string_expect_exception():
    with pytest.raises(TypeError):
        sum_two_element(4,'I do not have a number')
    