# door.py
class Door:
    def __init__(self):
        self.is_open = False

    def attempt_open(self, human):
        """Attempts to open the door if the human can do so."""
        if human.open_door():
            self.is_open = True
            return True
        return False
