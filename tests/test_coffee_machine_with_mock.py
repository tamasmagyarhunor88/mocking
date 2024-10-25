from lib.coffee_beans import CoffeeBeans
from lib.coffee_machine import CoffeeMachine
from unittest.mock import Mock


class TestCoffeeMachineWithMocking:
    def setup_method(self):
        self.machine = CoffeeMachine()
        self.mock_beans = Mock()
    
    def test_machine_works_with_good_beans(self):
        # Configure mock to simulate fresh beans that grind well
        self.mock_beans.grind.return_value = True
        
        # Test brewing
        assert self.machine.brew_coffee(self.mock_beans) is True
        assert self.machine.is_brewing is True
        
        # Verify grind was attempted
        self.mock_beans.grind.assert_called_once()
    
    def test_machine_fails_with_bad_beans(self):
        # Configure mock to simulate old beans that won't grind
        self.mock_beans.grind.return_value = False
        
        # Test brewing
        assert self.machine.brew_coffee(self.mock_beans) is False
        assert self.machine.is_brewing is False
        
        # Verify grind was attempted
        self.mock_beans.grind.assert_called_once()