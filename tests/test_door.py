# test_door.py
from unittest.mock import Mock
from lib.door import Door

def test_door_opens_with_eligible_human():
    # Create a mock Human who can open the door
    mock_human = Mock()
    mock_human.open_door.return_value = True
    
    # Create the door and attempt to open it
    door = Door()
    result = door.open(mock_human)
    
    # Assert that the door opens
    assert door.is_open == True
    assert result == True

def test_door_does_not_open_with_ineligible_human():
    # Create a mock Human who cannot open the door
    mock_human = Mock()
    mock_human.open_door.return_value = False
    
    # Create the door and attempt to open it
    door = Door()
    result = door.open(mock_human)
    
    # Assert that the door does not open
    assert door.is_open == False
    assert result == False
