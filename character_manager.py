"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: Brittney Rouse

AI Usage: [Document any AI assistance used]

This module handles character creation, loading, and saving.
"""

import os
import csv
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]
    
    # Raise InvalidCharacterClassError if class not in valid list
    character_class = input()
    character_level = 1
    character_experience = 0
    gold = 100
    inventory = []
    active_quests = []
    completed_quests = []

    if character_class == "Warrior":
        health = 120
        strength = 15
        magic = 5
        max_health = 360
    if character_class == "Mage":
        health = 80
        strength = 8
        magic = 20
        max_health = 240
    if character_class == "Rogue":
        health = 90
        strength = 12
        magic = 10
        max_health = 270
    if character_class == "Cleric":
        health = 100
        strength = 10
        magic = 15
        max_health = 300

    if character_class not in valid_classes:
        raise InvalidCharacterClassError

    character_data = {name, "Class": character_class, "Level": character_level, "Health": health, "Max health": max_health, "Strength": strength, "Magic": magic, "Experience":
character_experience, "Gold": gold, "Inventory": inventory, "Active quests": active_quests, "Completed quests": completed_quests}
        
    return character_data


def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    try:
        filename = {charater_name}_save.txt
        print(f"NAME: {character_name}")
        print(f"CLASS: {class_name}")
        print(f"LEVEL: {character_level}")
        print(f"HEALTH: {health}")
        print(f"MAX_HEALTH: {max_health}")
        print(f"STRENGTH: {strength}")
        print(f"MAGIC: {magic}")
        print(f"EXPERIENCE: {character_experience}")
        print(f"GOLD: {gold}")
        print(f"INVENTORY: {inventory}")
        print(f"ACTIVE QUESTS: {active_quests}")
        print(f"COMPLETED QUESTS: {completed_quests}")
    except:
        raise PermissionError
        raise IOError
    return True
    

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    # Check if file exists → CharacterNotFoundError
    # Try to read file → SaveFileCorruptedError
    # Validate data format → InvalidSaveDataError
    # Parse comma-separated lists back into Python lists
    raise CharacterNotFoundError
    raise SaveFileCorruptedError
    raise InvalidSaveDataError
    return character_data
    

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    all_saved_characters = character_data[name]
    if :
        all_saved_characters = []
    return all_saved_characters
    

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    try:
        if :
            raise CharacterNotFoundError
    return True
    

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
    level_up_xp = level * 100

    if (health > 0) and (character_experience >= level_up_xp):
        level += 1
        max_health += 10
        strength += 2
        magic += 2
        health = max_health
        character_experience = character_experience - level_up_xp
        continue
    if health == 0:
        raise CharacterDeadError
    

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
    gold += amount
    if gold < 0:
        raise ValueError
        
    return gold
    

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    health += amount
    if health > max_health:
        leftover_healing = health - max_health
        health = health - amount
        health = health + leftover_healing
    return health
    

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    if health > 0:
        return True
    else:
        return False

def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    health = max_health * .5
    return True

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    if len(character_data) < 12:
        raise InvalidSaveDataError
    if :
        raise InvalidSaveDataError
    if wasd:
        raise InvalidSaveDataError
    
    

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    # try:
    #     char = create_character("TestHero", "Warrior")
    #     print(f"Created: {char['name']} the {char['class']}")
    #     print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    # except InvalidCharacterClassError as e:
    #     print(f"Invalid class: {e}")
    
    # Test saving
    # try:
    #     save_character(char)
    #     print("Character saved successfully")
    # except Exception as e:
    #     print(f"Save error: {e}")
    
    # Test loading
    # try:
    #     loaded = load_character("TestHero")
    #     print(f"Loaded: {loaded['name']}")
    # except CharacterNotFoundError:
    #     print("Character not found")
    # except SaveFileCorruptedError:
    #     print("Save file corrupted")

