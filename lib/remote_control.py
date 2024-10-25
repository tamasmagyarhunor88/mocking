class RemoteControl():
    def __init__(self, battery_level: int):
        self.battery_level = battery_level
    
    def press_power_button(self) -> bool:
        # Remote won't work if batteries are too low (below 10%)
        return self.battery_level >= 10