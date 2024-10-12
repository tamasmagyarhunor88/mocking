# pokemon.py
class Pokemon:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other_pokemon):
        """Pokemon attacks another Pokemon"""
        other_pokemon.take_damage(self.attack_power)

    def is_fainted(self):
        """Check if the Pokemon has fainted"""
        return self.hp <= 0

    def take_damage(self, damage):
        """Pokemon takes damage"""
        self.hp -= damage