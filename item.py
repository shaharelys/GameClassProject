# item.py
from config import *


class Item:
    """
    The Item class represents an item in the game. It has a name, description, and power.
    """

    def __init__(self, name: str, description: str, power: int) -> None:
        """
        Initializes a new item with a name and a description.
        """
        self.name = name
        self.description = description
        self.power = power


class HealthPotion(Item):
    def __init__(self):
        super().__init__(name=HEALTH_POTION, description=DESC_HEALTH_POTION, power=VAL_HEALTH_POTION)


class Cloak(Item):
    def __init__(self):
        super().__init__(name=CLOAK, description=DESC_CLOAK, power=VAL_CLOAK)


class Gloves(Item):
    def __init__(self):
        super().__init__(name=GLOVES, description=DESC_GLOVES, power=VAL_GLOVES)


class Dagger(Item):
    def __init__(self):
        super().__init__(name=DAGGER, description=DESC_DAGGER, power=VAL_DAGGER)


class LoveStone(Item):
    def __init__(self):
        super().__init__(name=LOVE_STONE, description=DESC_LOVE_STONE, power=VAL_LOVE_STONE)


class WoodenShield(Item):
    def __init__(self):
        super().__init__(name=WOODEN_SHIELD, description=DESC_WOODEN_SHIELD, power=VAL_WOODEN_SHIELD)


class BloodPotion(Item):
    def __init__(self):
        super().__init__(name=BLOOD_POTION, description=DESC_BLOOD_POTION, power=VAL_BLOOD_POTION)


class TheWatchingEagle(Item):
    def __init__(self):
        super().__init__(name=THE_WATCHING_EAGLE, description=DESC_THE_WATCHING_EAGLE, power=VAL_THE_WATCHING_EAGLE)


class SacredHeart(Item):
    def __init__(self):
        super().__init__(name=SACRED_HEART, description=DESC_SACRED_HEART, power=VAL_SACRED_HEART)
