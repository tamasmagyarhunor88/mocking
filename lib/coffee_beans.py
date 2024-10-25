class CoffeeBeans:
    def __init__(self, days_since_roasted: int):
        self.days_since_roasted = days_since_roasted
    
    def grind(self) -> bool:
        # Beans that are too old (>30 days) become oily and can clog grinders
        return self.days_since_roasted <= 30