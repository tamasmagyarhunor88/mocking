from lib.coffee_beans import CoffeeBeans

class CoffeeMachine:
    def __init__(self):
        self.is_brewing = False
    
    def brew_coffee(self, beans: CoffeeBeans) -> bool:
        if beans.grind():
            self.is_brewing = True
            return True
        return False