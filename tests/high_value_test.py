from lib.high_value import *

def test_second_value_higher():
    get_highvalue = HighValue(2, 5)
    result = get_highvalue.get_highest()
    assert result == "Second value is higher"

def test_first_value_higher():
    get_highvalue = HighValue(5, 2)
    result = get_highvalue.get_highest()
    assert result == "First value is higher"

def test_values_are_equal():
    get_highvalue = HighValue(5, 5)
    result = get_highvalue.get_highest()
    assert result == "Values are equal"   


def test_increase_first():
    get_highvalue = HighValue(5, 2)
    get_highvalue.add(5, "first")
    assert get_highvalue.value_first == 10

def test_increase_second():
    get_highvalue = HighValue(5, 2)
    get_highvalue.add(5, "second")
    assert get_highvalue.value_second == 7


