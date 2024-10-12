# arena.py
class Arena:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def battle(self):
        """Simulates a battle between two Pokémon with attack logs"""
        while True:
            # Pokemon1 attacks first
            print(f"{self.pokemon1.name} attacks {self.pokemon2.name}!")
            self.pokemon1.attack(self.pokemon2)
            
            if self.pokemon2.is_fainted():
                if self.pokemon1.is_fainted():  # Check for draw
                    print(f"{self.pokemon2.name} and {self.pokemon1.name} both faint!")
                    return "It's a draw!"
                print(f"{self.pokemon2.name} faints! {self.pokemon1.name} wins!")
                return f"{self.pokemon1.name} wins!"

            # Pokemon2 attacks back
            print(f"{self.pokemon2.name} attacks {self.pokemon1.name}!")
            self.pokemon2.attack(self.pokemon1)

            if self.pokemon1.is_fainted():
                if self.pokemon2.is_fainted():  # Check for draw
                    print(f"{self.pokemon1.name} and {self.pokemon2.name} both faint!")
                    return "It's a draw!"
                print(f"{self.pokemon1.name} faints! {self.pokemon2.name} wins!")
                return f"{self.pokemon2.name} wins!"
