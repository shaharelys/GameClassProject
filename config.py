# config.py
"""Contains all program texts and the values"""

"""game"""
START_LOCATION_INDEX = 0
START_DIVIDER = "-"*30+"\tGET READY!\t"+"-"*30 + "\n\n"
START_MSG = "Welcome, courageous traveler, to 'The Hunt for The Great Monster'!\n\n"\
            "In this world of treacherous landscapes and daunting adversaries, you stand as a beacon of hope.\n" \
            "You are not just an adventurer; you are a protector, a savior. Born and raised in a tranquil village\n" \
            "that now teeters on the brink of despair, a great responsibility rests upon your sturdy shoulders. \n\n"\
            "Rumors of a Great Monster have spread like wildfire, stoking fear in the hearts of the villagers.\n" \
            "This monstrous creature, a being of untold power and malevolence, has claimed a dark castle as\n" \
            "its lair. Your people live each day under the shadow of its impending wrath. Yet, where others see an\n" \
            "insurmountable threat, you see a challenge that needs to be met, a wrong that needs to be righted. \n\n"\
            "As you embark on this perilous journey, remember that bravery is not the absence of fear, but the will\n" \
            "to confront it. May your heart be your guiding key as you venture forth to save your village from the\n" \
            "looming darkness. Let the Hunt for The Great Monster begin!\n\n\n" + START_DIVIDER
OP1, OP2, OP3, OP4 = "1", "2", "3", "4"
PLAY_TURN_MENU = f"\nWhat would you like to do?\n" \
                 f"{OP1}. Get informed\n" \
                 f"{OP2}. Move to the next location\n" \
                 f"{OP3}. Use an item\n" \
                 f"{OP4}. Attack an enemy"
PLAY_TURN_ACT2_MSG1 = "You can't move in that direction."
PLAY_TURN_ACT2_MSG2 = "You can't move before defeating the {}."
PLAY_TURN_ACT3_MSG2 = "You don't have any items."
PLAY_TURN_ACT3_MSG3 = "Which item would you like to use?"
PLAY_TURN_ACT4_MSG0 = "You are confronting the {}!"
PLAY_TURN_ACT4_MSG1 = "There are no enemies here."
ENTER_LOCATION_MSG1 = "You found an item, {}, {} Its power equals {}."
ENTER_LOCATION_MSG2 = "You encountered an enemy, {}, {} Its health equals {}, its attack equals {}."
INFORM_MSG0 = "Your health is {}, your attack is {}.\n"
INFORM_MSG1 = "You have the following items:"
INFORM_MSG2 = "{}. {}, with power {}. {}"
INFORM_MSG3 = "You do not possess any items."
INFORM_MSG4 = "\nThere is an enemy here! {}, with health {} and attack {}.\nDescription: {}"
INFORM_MSG5 = "\nThere are no enemies here. You can move to the next location!"
GAME_OVER_MSG = "Game over."
WIN_MSG = "You have saved your village!\nCongratulations! You won the game!\n"
LOSE_MSG = "You have lost the game.\n"

"""locations"""
VILLAGE = "Village"
FOREST = "Forest"
MOUNTAIN = "Mountain"
CASTLE = "Castle"
UNKNOWN_LOCATION = "Unknown location"
LOCATION_TYPES = [VILLAGE, FOREST, MOUNTAIN, CASTLE]
DESC_VILLAGE = "You stand amidst the familiar surroundings of your childhood village, the place where your story\n" \
               "began. There's a comforting presence of friends and family around you, their faces reflecting a mix\n" \
               "of fear and hope. Yet, time is a luxury you can't afford. A monstrous creature is preparing to\n" \
               "descend upon your home, and you are the village's only defense. A dense fog descends, obscuring your\n" \
               "vision of what lies ahead. You squint through the mist to glimpse your next destination - a forest,\n" \
               "shrouded in mystery and danger, to the north. Within its depths dwell Orcs and Goblins, ruthless\n" \
               "entities that you must confront and defeat on your quest. Be ready, your journey is just beginning.\n"
DESC_FOREST = "You've stepped into the heart of a dense, shadowy forest. The air is thick with the scent of pine\n" \
              "and damp earth. Sounds of nocturnal creatures echo through the rustling leaves, while the distant\n" \
              "howls of wolves send chills down your spine. Danger could lurk behind any tree, as this woodland is\n" \
              "known to be ruled by Orcs and Goblins. Prepare yourself for the battles ahead.\n"
DESC_MOUNTAIN = "You find yourself at the base of a colossal mountain. Its towering peaks seem to scrape the sky,\n" \
                "while the icy air feels thin and scarce. The biting cold pierces your bones, and the terrain is\n" \
                "rugged and treacherous. Each step echoes in the deafening silence of the altitude. This mountain\n" \
                "path, full of hidden perils, leads you towards your destination.\n"
DESC_CASTLE = "You've finally reached the ominous dark castle. Its menacing silhouette stretches against the night\n" \
              "sky, and the heavy iron gates creak open to welcome you into a world of lurking danger. Shadows play\n" \
              "tricks on your eyes, and the echoes of haunting whispers fill the cold, stone corridors. Every corner\n" \
              "could hide a monstrous enemy, so tread lightly and keep your guard up.\n"

"""items"""
RANDOM_ITEM = "Random Item"
HEALTH_POTION = "Health Potion"
CLOAK = "Cloak"
GLOVES = "Gloves"
DAGGER = "Dagger"
LOVE_STONE = "Love Stone"
WOODEN_SHIELD = "Wooden Shield"
BLOOD_POTION = "Blood Potion"
THE_WATCHING_EAGLE = "The Watching Eagle"
SACRED_HEART = "Sacred Heart"
UNKNOWN_ITEM = "Unknown Item"
ITEM_TYPES = [RANDOM_ITEM,
              # Village item types
              CLOAK,
              GLOVES,
              DAGGER,
              # Forest item types
              LOVE_STONE,
              HEALTH_POTION,
              WOODEN_SHIELD,
              # Mountain item types
              BLOOD_POTION,
              THE_WATCHING_EAGLE,
              SACRED_HEART
              ]
VILLAGE_ITEM_TYPES = [CLOAK, GLOVES, DAGGER]
FOREST_ITEM_TYPES = [LOVE_STONE, HEALTH_POTION, WOODEN_SHIELD]
MOUNTAIN_ITEM_TYPES = [BLOOD_POTION, THE_WATCHING_EAGLE, SACRED_HEART]
CASTLE_ITEM_TYPES = None  # No items in the castle

DESC_HEALTH_POTION = "A potion that can restore health."
DESC_CLOAK = "A cloak that provides protection from the elements."
DESC_GLOVES = "A pair of gloves that can protect your hands."
DESC_DAGGER = "A sharp dagger that can be used for close combat."
DESC_LOVE_STONE = "A magical stone that is said to make enemies fall in love and influence their actions."
DESC_WOODEN_SHIELD = "A shield made of sturdy wood that can block attacks."
DESC_BLOOD_POTION = "A potion that can increase your attack power."
DESC_THE_WATCHING_EAGLE = "A mythical eagle that can scout the area."
DESC_SACRED_HEART = "A sacred heart that can provide healing power."

VAL_CLOAK = 10
VAL_GLOVES = 10
VAL_DAGGER = 25
VAL_WOODEN_SHIELD = 20
VAL_LOVE_STONE = 40
VAL_HEALTH_POTION = 50
VAL_BLOOD_POTION = 40
VAL_THE_WATCHING_EAGLE = 60
VAL_SACRED_HEART = 75

"""enemies"""
RANDOM_ENEMY = "Random Enemy"
GOBLIN = "Goblin"
ORC = "Orc"
RED_EYED_OWL = "Red-Eyed Owl"
BLOODY_WORM = "Bloody Worm"
THE_GREAT_MONSTER = "Great Monster"
UNKNOWN_ENEMY = "Unknown Enemy"
ENEMY_TYPES = [RANDOM_ENEMY,
               # Forest enemy types
               GOBLIN,
               ORC,
               # Mountain enemy types
               RED_EYED_OWL,
               BLOODY_WORM,
               # Castle enemy types
               THE_GREAT_MONSTER
               ]
VILLAGE_ENEMY_TYPES = None  # No enemies in the village
FOREST_ENEMY_TYPES = [GOBLIN, ORC]
MOUNTAIN_ENEMY_TYPES = [RED_EYED_OWL, BLOODY_WORM]
CASTLE_ENEMY_TYPES = [THE_GREAT_MONSTER]
DESC_GOBLIN = "A small, mischievous creature."
DESC_ORC = "A large, brutish creature."
DESC_RED_EYED_OWL = "A mystical owl with glowing red eyes."
DESC_BLOODY_WORM = "A gigantic worm that lives underground."
DESC_THE_GREAT_MONSTER = "A monstrous creature that rules the castle."

VAL_GOBLIN_HEALTH = 50
VAL_GOBLIN_ATTACK = 10
VAL_ORC_HEALTH = 80
VAL_ORC_ATTACK = 20
VAL_RED_EYED_OWL_HEALTH = 60
VAL_RED_EYED_OWL_ATTACK = 15
VAL_BLOODY_WORM_HEALTH = 80
VAL_BLOODY_WORM_ATTACK = 25
VAL_THE_GREAT_MONSTER_HEALTH = 100
VAL_THE_GREAT_MONSTER_ATTACK = 40

"""player"""
CONFRONT_MSG1 = "Good Job! You have defeated the {}!"
CONFRONT_MSG2 = "You have been defeated by the {}."
CONFRONT_MSG3 = "You did not defeat the {}. It has {} health left. You have {} health left."
MOVE_MSG1 = "You are now on your way from the {} to the {}!"
USE_MSG1 = "You have used the {}! You gained {} health points and you now have {} health."

"""general"""
UNKNOWN_TYPE = "Unknown Type"
