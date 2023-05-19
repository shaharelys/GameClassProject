# commands.py
from abc import ABC, abstractmethod
from config import *

"""
def play_turn(self) -> None:
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
                print(INPUT_ERROR_MSG)

    elif action == OP4:
        if enemies:
            print(PLAY_TURN_ACT4_MSG0.format(enemies[0].name))
            self.player.confront(enemies[0])
        else:
            print(PLAY_TURN_ACT4_MSG1)
"""


class ICommand(ABC):
    """
    Abstract base class for all commands.
    """
    @abstractmethod
    def execute(self):
        pass


class InformCommand(ICommand):
    """
    Concrete Command class for the inform action.
    """
    def __init__(self, game):
        self.game = game

    def execute(self):
        self.game.inform(self.game.player.location)


class MoveCommand(ICommand):
    """
    Concrete Command class for the move action.
    """
    def __init__(self, game):
        self.game = game

    def execute(self):
        current_location = self.game.player.location
        enemies = current_location.enemies
        game_locations = self.game.locations

        if not current_location.name == CASTLE:
            if enemies:
                print(PLAY_TURN_ACT2_MSG2.format(enemies[0].name))
            else:
                self.game.player.move(game_locations[current_location.index + 1])
                new_location = self.game.player.location
                self.game.enter_location(new_location)
        else:
            print(PLAY_TURN_ACT2_MSG1)


class UseItemCommand(ICommand):
    """
    Concrete Command class for the use item action.
    """
    def __init__(self, game):
        self.game = game

    def execute(self):
        if not self.game.player.inventory:
            print(PLAY_TURN_ACT3_MSG2)
        else:
            print(PLAY_TURN_ACT3_MSG3)
            for i, item in enumerate(self.game.player.inventory, 1):
                print(f"{i}. {item.name}")
            try:
                item_number = int(input("> ")) - 1
                self.game.player.use(self.game.player.inventory[item_number])
            except ValueError:
                print(INPUT_ERROR_MSG)


class ConfrontCommand(ICommand):
    """
    Concrete Command class for the confront action.
    """
    def __init__(self, game):
        self.game = game

    def execute(self):
        enemies = self.game.player.location.enemies
        if enemies:
            print(PLAY_TURN_ACT4_MSG0.format(enemies[0].name))
            self.game.player.confront(enemies[0])
        else:
            print(PLAY_TURN_ACT4_MSG1)
