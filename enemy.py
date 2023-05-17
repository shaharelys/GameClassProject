# enemy.py
from config import *


class Enemy:
    """
    The Enemy class represents an enemy in the game. It has a name, a description, health, and attack strength.
    """

    def __init__(self, name: str, description: str, health: int, attack: int) -> None:
        """
        Initializes a new enemy with a name, a description, health, and attack strength.
        """
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name=GOBLIN, description=DESC_GOBLIN, health=VAL_GOBLIN_HEALTH, attack=VAL_GOBLIN_ATTACK)


class Orc(Enemy):
    def __init__(self):
        super().__init__(name=ORC, description=DESC_ORC, health=VAL_ORC_HEALTH, attack=VAL_ORC_ATTACK)


class RedEyedOwl(Enemy):
    def __init__(self):
        super().__init__(name=RED_EYED_OWL, description=DESC_RED_EYED_OWL, health=VAL_RED_EYED_OWL_HEALTH, attack=VAL_RED_EYED_OWL_ATTACK)


class BloodyWorm(Enemy):
    def __init__(self):
        super().__init__(name=BLOODY_WORM, description=DESC_BLOODY_WORM, health=VAL_BLOODY_WORM_HEALTH, attack=VAL_BLOODY_WORM_ATTACK)


class TheGreatMonster(Enemy):
    def __init__(self):
        super().__init__(name=THE_GREAT_MONSTER, description=DESC_THE_GREAT_MONSTER, health=VAL_THE_GREAT_MONSTER_HEALTH, attack=VAL_THE_GREAT_MONSTER_ATTACK)

