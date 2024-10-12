# test_arena.py
import pytest
from unittest.mock import Mock
from lib.arena import Arena

def test_arena_battle_pokemon1_wins():
    # Create mock objects for Pokemon
    mock_pokemon1 = Mock()
    mock_pokemon2 = Mock()

    # Set up mock behaviors
    mock_pokemon1.name = "Pikachu"
    mock_pokemon2.name = "Charizard"

    # Simulate the battle sequence
    mock_pokemon1.is_fainted.side_effect = [False, False, True]  # Pikachu wins after 3 attacks
    mock_pokemon2.is_fainted.side_effect = [False, True]         # Charizard faints after 2 attacks

    # We must mock attack to avoid real logic
    mock_pokemon1.attack = Mock()
    mock_pokemon2.attack = Mock()

    # Create the Arena object with the mocked Pokemon
    arena = Arena(mock_pokemon1, mock_pokemon2)

    # Call the battle method and verify the result
    result = arena.battle()
    assert result == "Pikachu wins!"

def test_arena_battle_pokemon1_wins():
    mock_pokemon1 = Mock()
    mock_pokemon2 = Mock()

    # Set up Pokemon names
    mock_pokemon1.name = "Pikachu"
    mock_pokemon2.name = "Charizard"

    # Set up mock behaviors for is_fainted
    mock_pokemon1.is_fainted.side_effect = [False, False, True]  # Faints after 3 attacks
    mock_pokemon2.is_fainted.side_effect = [False, True]         # Faints after 2 attacks

    # Mock the attack methods (do nothing)
    mock_pokemon1.attack = Mock()
    mock_pokemon2.attack = Mock()

    # Create the arena with mocked Pokemon
    arena = Arena(mock_pokemon1, mock_pokemon2)

    # Run battle and check result
    result = arena.battle()
    assert result == "Pikachu wins!"

def test_arena_battle_draw():
    # Create mock objects for Pokemon
    mock_pokemon1 = Mock()
    mock_pokemon2 = Mock()

    # Set up mock behaviors
    mock_pokemon1.name = "Eevee"
    mock_pokemon2.name = "Pidgey"

    # Simulate both fainting at the same time
    mock_pokemon1.is_fainted.side_effect = [False, True]
    mock_pokemon2.is_fainted.side_effect = [False, True]

    # Mock attack methods to avoid real logic
    mock_pokemon1.attack = Mock()
    mock_pokemon2.attack = Mock()

    # Create the Arena object with the mocked Pokemon
    arena = Arena(mock_pokemon1, mock_pokemon2)

    # Call the battle method and verify the result
    result = arena.battle()
    assert result == "It's a draw!"
