# test_human.py
from lib.human import Human

def test_human_can_open_door():
    # Test for a human that is old enough (3 years and older)
    adult = Human(age=5)
    assert adult.open_door() == True

def test_human_cannot_open_door():
    # Test for a human that is too young (less than 3 years old)
    toddler = Human(age=2)
    assert toddler.open_door() == False
