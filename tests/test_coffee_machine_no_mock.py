from lib.coffee_beans import CoffeeBeans
from lib.coffee_machine import CoffeeMachine

class TestCoffeeMachineWithoutMocking:
    def setup_method(self):
        self.machine = CoffeeMachine()
    
    def test_machine_brews(self):
        fresh_beans = CoffeeBeans(5)  # 5 days old
        assert self.machine.brew_coffee(fresh_beans) is True
        assert self.machine.is_brewing is True
    
    # This test will fail if CoffeeBeans.grind logic changes!
    def test_machine_wont_brew(self):
        old_beans = CoffeeBeans(45)  # 45 days old
        assert self.machine.brew_coffee(old_beans) is False
        assert self.machine.is_brewing is False