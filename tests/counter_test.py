from lib.counter import *

def test_add_adds_number_to_count():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_report_returns_string():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 3 so far."

