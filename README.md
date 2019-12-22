# Python3 : RPG
## Create  RPG in Python.
Rpg create as a team Farid and Nicolas

## Presentation

This rpg is a game project representing a turn-based rpg
we created it with a class for each character
we also created a common class and the at the creation of a people object is class inherited from
the common class.

we created game objects to reuse them during combat
as well as objects for narration and time sleep clear to clear the screen as a transition.

## progress

- The player can choose the type of character he wishes to embody
- Three classes are available for the player (warrior, archer, magician)
- The player can name his character as he wishes at the start of the game
- Three classes are available for enemies (orc, wolf, zombie)
- The characters all have at least the following characteristics (life, attack, defense, agility, name)
- The magician also has mana representing his magic force
- A character can attack another, the target then loses life in proportion to its defense value and the attacker's attack value
- The magician can heal himself. This spell consumes mana but gives it new life. If he doesn't have enough mana, he can't cast it
- A fight is simulated between the player character and an enemy of your choice until either character is dead.
## Quality criteria
Technical specifications :
- Python 3 language
- Code organization in modules and packages
- Use of object oriented programming
- Respect for the DRY principle
- Try to respect some of the SOLID principles
- Program executable by launching a main.py file
Resources
https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232721-apprehendez-les-classes
