from lib.pokemon import Pokemon

def test_pokemon_instantiates_with_attributes():
    pikachu = Pokemon('Pikachu', 100, 20)
    
    assert pikachu.name == 'Pikachu'
    assert pikachu.hp == 100
    assert pikachu.attack_power == 20

def test_pokemon_attacks_other_pokemon():
    pikachu = Pokemon('Pikachu', 100, 20)
    bulbasaur = Pokemon('Bulbasaur', 100, 25)

    pikachu.attack(bulbasaur)
    bulbasaur.attack(pikachu)

    assert bulbasaur.hp == 80
    assert pikachu.hp == 75

def test_pokemon_take_damage():
    pikachu = Pokemon('Pikachu', 100, 20)

    pikachu.take_damage(13)

    assert pikachu.hp == 87

def test_pokemon_is_fainted():
    pikachu = Pokemon('Pikachu', 100, 20)
    pikachu.take_damage(100)

    assert pikachu.is_fainted()