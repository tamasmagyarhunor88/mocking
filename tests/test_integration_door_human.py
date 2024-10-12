# test_integration_door_human.py
from lib.door import Door
from lib.human import Human

def test_integration_door_opens_with_adult():
    # Create a Human who is old enough to open the door
    adult = Human(age=5)
    door = Door()
    
    # Human attempts to open the door
    result = door.attempt_open(adult)
    
    # Assert that the door opens
    assert door.is_open == True
    assert result == True

def test_integration_door_does_not_open_with_toddler():
    # Create a Human who is too young to open the door
    toddler = Human(age=2)
    door = Door()
    
    # Human attempts to open the door
    result = door.attempt_open(toddler)
    
    # Assert that the door does not open
    assert door.is_open == False
    assert result == False

def test_integration_door_opens_with_exactly_3yo():
    # Create a Human who is exactly 3 years old
    young_human = Human(age=3)
    door = Door()
    
    # Human attempts to open the door
    result = door.attempt_open(young_human)
    
    # Assert that the door opens since the human is 3yo or older
    assert door.is_open == True
    assert result == True
