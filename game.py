# game.py
from factory import LocationFactory, ItemFactory, EnemyFactory
from player import Player
from location import Location
from config import *


class Game:
    """
    The Game class controls the flow of the game.
    It keeps track of the current state of the game and handles the main game loop.
    """

    def __init__(self) -> None:
        """
        Initializes a new game.
        Creates a Player object and the different Location objects, and sets the starting location.
        """
        self.player = Player()
        self.locations = self.create_locations()
        self.player.location = self.locations[START_LOCATION_INDEX]

    def create_locations(self) -> list[Location]:
        """
        Creates the locations for the game.
        """
        locations = [LocationFactory.create_location(location_type=VILLAGE),
                     LocationFactory.create_location(location_type=FOREST),
                     LocationFactory.create_location(location_type=MOUNTAIN),
                     LocationFactory.create_location(location_type=CASTLE)]
        return locations

    def start(self) -> None:
        """
        Starts the game. Displays the introductory text and enters the main game loop.
        """
        print(START_MSG)
        self.enter_location(self.player.location)
        while not self.game_over():
            self.play_turn()

    def play_turn(self) -> None:
        """
        Handles the logic for each turn of the game.
        """

        # Simplified objects for readability
        player = self.player
        current_location = self.player.location
        enemies = self.player.location.enemies
        game_locations = self.locations

        print(PLAY_TURN_MENU)  # player chooses from OP1, OP2, OP3, OP4
        action = input("> ")

        if action == OP1:
            self.inform(current_location)

        elif action == OP2:
            if not current_location.name == CASTLE:
                if enemies:
                    # Have to defeat the enemy before moving to the next location
                    print(PLAY_TURN_ACT2_MSG2.format(enemies[0].name))
                else:
                    player.move(game_locations[current_location.index + 1])
                    new_location = player.location
                    self.enter_location(new_location)
            else:
                print(PLAY_TURN_ACT2_MSG1)

        elif action == OP3:
            if not self.player.inventory:
                print(PLAY_TURN_ACT3_MSG2)
            else:
                print(PLAY_TURN_ACT3_MSG3)
                for i, item in enumerate(self.player.inventory, 1):
                    print(f"{i}. {item.name}")
                try:
                    item_number = int(input("> ")) - 1
                    self.player.use(self.player.inventory[item_number])
                except ValueError:
                    print("Please enter a valid number.")

        elif action == OP4:
            if enemies:
                print(PLAY_TURN_ACT4_MSG0.format(enemies[0].name))
                self.player.confront(enemies[0])
            else:
                print(PLAY_TURN_ACT4_MSG1)

    def enter_location(self, location: Location) -> None:
        """
        Handles the player entering a new location.
        """
        print(location.description)

        # Add random item to location and player's inventory
        if location.name != CASTLE:
            if not location.items:
                random_item = ItemFactory.create_item(RANDOM_ITEM, location)
                location.items.append(random_item)
                self.player.inventory.append(random_item)
            for item in location.items:
                print(ENTER_LOCATION_MSG1.format(item.name, item.description, item.power))

        # Add random enemy to location
        if location.name != VILLAGE:
            if not location.enemies:
                random_enemy = EnemyFactory.create_enemy(RANDOM_ENEMY, location)
                location.enemies.append(random_enemy)
            for enemy in location.enemies:
                print(ENTER_LOCATION_MSG2.format(enemy.name, enemy.description, enemy.health, enemy.attack))

    def inform(self, location: Location) -> None:
        # Inform player of location and overall details
        print(location.description)
        print(INFORM_MSG0.format(self.player.health, self.player.attack))

        # Print player's inventory information
        if self.player.inventory:
            print(INFORM_MSG1)
            for i, item in enumerate(self.player.inventory, 1):
                print(INFORM_MSG2.format(i, item.name, item.power, item.description))
        else:
            print(INFORM_MSG3)

        # Print location's enemies information
        if location.enemies:
            enemy = location.enemies[0]
            print(INFORM_MSG4.format(enemy.name, enemy.health, enemy.attack, enemy.description))
        else:
            print(INFORM_MSG5)

    def game_over(self) -> bool:
        """
        Checks if the game is over.
        """

        if self.player.health <= 0:
            print(LOSE_MSG+GAME_OVER_MSG)
            return True

        if self.player.location.name == CASTLE and not self.player.location.enemies:
            print(WIN_MSG+GAME_OVER_MSG)
            return True
        return False
