# factory.py
from item import *
from enemy import *
from location import *
from config import *
import random

"""Contains the factory classes for creating items, enemies, and locations in a game."""

class ItemFactory:

    @staticmethod
    def create_item(item_type: str, location: Location) -> Item:
        if item_type == RANDOM_ITEM:
            item_type = random.choice(location.item_types)
        if item_type == HEALTH_POTION:
            return HealthPotion()
        elif item_type == CLOAK:
            return Cloak()
        elif item_type == GLOVES:
            return Gloves()
        elif item_type == DAGGER:
            return Dagger()
        elif item_type == LOVE_STONE:
            return LoveStone()
        elif item_type == WOODEN_SHIELD:
            return WoodenShield()
        elif item_type == BLOOD_POTION:
            return BloodPotion()
        elif item_type == THE_WATCHING_EAGLE:
            return TheWatchingEagle()
        elif item_type == SACRED_HEART:
            return SacredHeart()
        else:
            raise ValueError(UNKNOWN_ITEM)


class EnemyFactory:

    @staticmethod
    def create_enemy(enemy_type: str, location: Location) -> Enemy:
        if enemy_type == RANDOM_ENEMY:
            enemy_type = random.choice(location.enemy_types)
        if enemy_type == GOBLIN:
            return Goblin()
        elif enemy_type == ORC:
            return Orc()
        elif enemy_type == RED_EYED_OWL:
            return RedEyedOwl()
        elif enemy_type == BLOODY_WORM:
            return BloodyWorm()
        elif enemy_type == THE_GREAT_MONSTER:
            return TheGreatMonster()
        else:
            raise ValueError(enemy_type + ' : ' + UNKNOWN_ENEMY)


class LocationFactory:

    @staticmethod
    def create_location(location_type: str) -> Location:
        if location_type == VILLAGE:
            return Village()
        elif location_type == FOREST:
            return Forest()
        elif location_type == MOUNTAIN:
            return Mountain()
        elif location_type == CASTLE:
            return Castle()
        else:
            raise ValueError(UNKNOWN_LOCATION)

