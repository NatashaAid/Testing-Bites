from lib.string_builder import *

def test_add_string():
    string = StringBuilder()
    string.add("2, 3, 4")
    assert string.output() == "2, 3, 4"

def test_check_string_length():
    string = StringBuilder()
    string.add("hello")
    result = string.size() 
    assert result == 5

