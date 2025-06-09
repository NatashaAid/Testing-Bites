from lib.most_often import *


def test_add_new():
    starting_list = ['hat', 'glasses']
    new_list = MostOften(starting_list)
    new_list.add_new('shoes')
    assert new_list.starting_list == ['hat', 'glasses', 'shoes']


def test_add_multiple_new():
    starting_list = ['hat', 'glasses']
    new_list = MostOften(starting_list)
    new_list.add_new('shoes')
    new_list.add_new('keys')
    new_list.add_new('phone')
    assert new_list.starting_list == ['hat', 'glasses', 'shoes', 'keys', 'phone']


def test_get_often():
    starting_list = ['hat', 'glasses', 'hat', 'shoes']
    new_list = MostOften(starting_list)
    assert new_list.get_most_often() == 'hat'

def test_no_winner():
    starting_list = ['hat', 'glasses', 'hat', 'glasses', 'shoes']
    new_list = MostOften(starting_list)
    assert new_list.get_most_often() == "no clear winner"
