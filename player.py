# player.py
from item import Item
from location import Location

# player.py
from item import Item
from location import Location
from config import *


class Player:
    """
    The Player class represents the player. It keeps track of the player's health, inventory, and current location.
    """

    def __init__(self) -> None:
        """
        Initializes a new player with a starting health and an empty inventory.
        """
        self.health = 100
        self.attack = 30
        self.inventory = []
        self.location = None

    def confront(self, enemy) -> None:
        """
        Attacks an enemy.
        """

        # Player attacks first
        enemy.health -= self.attack
        if enemy.health <= 0:
            self.location.enemies.remove(enemy)
            print(CONFRONT_MSG1.format(enemy.name))
            return

        # Enemy attacks back
        self.health -= enemy.attack
        if self.health <= 0:
            print(CONFRONT_MSG2.format(enemy.name))
            return

        if enemy.health > 0 and self.health > 0:
            print(CONFRONT_MSG3.format(enemy.name, enemy.health, self.health))

    def move(self, new_location: Location) -> None:
        """
        Moves the player to a new location.
        """
        print(MOVE_MSG1.format(self.location.name, new_location.name))
        self.location = new_location

    def use(self, item: Item) -> None:
        """
        Uses an item from the player's inventory.
        """
        if item in self.inventory:
            self.health += item.power
            print(USE_MSG1.format(item.name, item.power, self.health))
            self.inventory.remove(item)
            return
