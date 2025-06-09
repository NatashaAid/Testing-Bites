from lib.greet import *

def test_greet_returns_greeting():
 result = greet("natasha")
 assert result == "Hello, natasha!"