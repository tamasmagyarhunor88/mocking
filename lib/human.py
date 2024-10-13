# human.py
class Human:
    def __init__(self, age):
        self.age = age

    def open_door(self):
        """Attempts to open the door."""
        if self.__can_pull_door_lever():
            return True
        return False

    def __can_pull_door_lever(self):
        """Returns True if the human can reach the lever, based on age."""
        return self.age >= 3
