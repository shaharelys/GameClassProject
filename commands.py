# commands.py
from abc import ABC, abstractmethod
from config import *


class ICommand(ABC):
    """
    Abstract base class for all commands.
    """
    @abstractmethod
    def execute(self) -> None:
        pass


class InformCommand(ICommand):
    """
    Concrete Command class for the inform action.
    """
    def __init__(self, game) -> None:
        self.game = game

    def execute(self) -> None:
        self.game.inform(self.game.player.location)


class MoveCommand(ICommand):
    """
    Concrete Command class for the move action.
    """
    def __init__(self, game) -> None:
        self.game = game

    def execute(self) -> None:
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
    def __init__(self, game) -> None:
        self.game = game

    def execute(self) -> None:
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
    def __init__(self, game) -> None:
        self.game = game

    def execute(self) -> None:
        enemies = self.game.player.location.enemies
        if enemies:
            print(PLAY_TURN_ACT4_MSG0.format(enemies[0].name))
            self.game.player.confront(enemies[0])
        else:
            print(PLAY_TURN_ACT4_MSG1)
