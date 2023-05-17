# location.py
from item import Item
from enemy import Enemy
from config import *


class Location:
    """
    The Location class represents a location in the game. It contains a description of the location, a list of items,
    and a list of enemies.
    """

    # Variables
    item_types = list[str]
    enemy_types = list[str]

    def __init__(self, name: str, index: int, description: str, items: list[Item], enemies: list[Enemy]) -> None:
        """
        Initializes a new location with a description, a list of items, and a list of enemies.
        """
        self.name = name
        self.index = index
        self.description = description
        self.items = items
        self.enemies = enemies


class Village(Location):

    # Variables
    item_types = VILLAGE_ITEM_TYPES
    enemy_types = VILLAGE_ENEMY_TYPES

    def __init__(self):
        super().__init__(name=VILLAGE, index=0, description=DESC_VILLAGE, items=[], enemies=[])


class Forest(Location):

    # Variables
    item_types = FOREST_ITEM_TYPES
    enemy_types = FOREST_ENEMY_TYPES

    def __init__(self):
        super().__init__(name=FOREST, index=1, description=DESC_FOREST, items=[], enemies=[])


class Mountain(Location):

    # Variables
    item_types = MOUNTAIN_ITEM_TYPES
    enemy_types = MOUNTAIN_ENEMY_TYPES

    def __init__(self):
        super().__init__(name=MOUNTAIN, index=2, description=DESC_MOUNTAIN, items=[], enemies=[])


class Castle(Location):

    # Variables
    item_types = CASTLE_ITEM_TYPES
    enemy_types = CASTLE_ENEMY_TYPES

    def __init__(self):
        super().__init__(name=CASTLE, index=3, description=DESC_CASTLE, items=[], enemies=[])
