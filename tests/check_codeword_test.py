from lib.check_codeword import *

def test_check_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_close():
    result = check_codeword("huge")
    assert result == "Close, but nope."

def test_check_codeword_wrong():
    result = check_codeword("apple")
    assert result == "WRONG!"