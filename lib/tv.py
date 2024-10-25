from lib.remote_control import RemoteControl

class TV():
    def __init__(self):
        self.is_on = False
    
    def power_toggle(self, remote: RemoteControl) -> bool:
        if remote.press_power_button():
            self.is_on = not self.is_on
            return True
        return False