# The Hunt for The Great Monster

## Introduction

Welcome to "The Hunt for The Great Monster" - a thrilling text-based adventure game where you, the player, embark on a perilous journey to save your tranquil village from a monstrous creature. 

In this immersive game, you will traverse through various locations, confront formidable enemies, and discover useful items that will aid you in your quest. Your decisions and strategy will shape the outcome of the game, ultimately leading to your victory or defeat.

## Game Structure
The game comprises several Python files, each with a specific responsibility:
1. `main.py`: The entry point of the game. This script initiates the game and controls the game flow.
2. `game.py`: Defines the game's main loop and handles the player's actions and responses.
3. `player.py`: Specifies the player's character, including attributes like health and attack power, and maintains the player's inventory.
4. `item.py`: Describes the different items discoverable in the game, each with unique properties.
5. `enemy.py`: Outlines the enemies in the game, each with unique health and attack characteristics.
6. `location.py`: Delineates the various locations in the game, each having a unique description, a potential item, and a potential enemy.
7. `factory.py`: Responsible for creating the game objects such as items, enemies, and locations.
8. `config.py`: Houses all the game's texts and values, ensuring a consistent and immersive gaming experience.

## Gameplay
In "The Hunt for The Great Monster," your journey begins in your home village. From there, you will navigate through a forest, climb a mountain, and finally arrive at a castle - the lair of the Great Monster. 
Each location may harbor an enemy, and you must vanquish them to move forward. Along the way, you may also stumble upon items that can assist you in your mission, such as health potions, weapons, and protective gear.

On each turn, you can choose from a menu of actions:
- Get information about your status and the current location
- Move to the next location
- Use an item from your inventory
- Attack an enemy

The game concludes when you defeat the Great Monster or when you lose all your health.

Installation and Running the Game
This game requires Python 3.6 or later. Download or clone this repository, navigate to the repository directory, and run the following command in your terminal to start the game:
python main.py