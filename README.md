# ZombieInMyPocket
### BCDE321 Advance Programming - Assignment 3 (Portfolio)

This repository is forked from [Fallen-Pie/ZombieInMyPocket](https://github.com/Fallen-Pie/ZombieInMyPocket) shared repository, `development/iteration-two` branch.

---

**To clone the forked repository, run:**
```shell
git clone https://github.com/arsenie-sarmiento/ZombieInMyPocket.git
```


**Run this command to switch to `ass3/portfolio` branch**
```shell
git checkout ass3/portfolio
```

---
### File Structure
```
ZombieInMyPocket/
├─ .gitignore
├─ src/
│ ├─ __init__.py                            [empty]
│ ├─ model/
│ │ ├─ game_time/                           [target block's component]
| │ │ ├─ __init__.py
│ | │ └─ game_time.py
│ │ ├─ combat/                              [target block's component]
| │ │ ├─ __init__.py
│ | │ └─ combat.py
│ │ ├─ interfaces/
| │ │ ├─ i_combat.py
| │ │ └─ __init__.py
│ │ ├─ __init__.py
| │ └─ before_pattern.drawio                [UML Class Diagram]
| |
│ └─ model_after_pattern/                   [refactored]
│   ├─ enums/
|   │   ├─ combat_option.py
|   │   └─ __init__().py
│   ├─ interfaces/
|   │   ├─ combat_strategy.py               [Strategy]
|   │   ├─ game_time_component.py           [Component Interface]
|   │   └─ __init__().py
│   ├─ game_time/
|   │   ├─ game_time.py                     [Concrete Component]
|   │   ├─ base_decorator.py                [Decorator]
|   │   ├─ custom_message_decorator.py      [Concrete Decorator]
|   │   ├─ format_decorator.py              [Concrete Decorator]
|   │   └─ __init__().py
│   ├─ combat/
|   │   ├─ combat.py                        [Context]
|   │   ├─ cower_strategy.py                [Concrete Strategy]
|   │   ├─ runaway_strategy.py              [Concrete Strategy]
|   │   ├─ engage_strategy.py               [Concrete Strategy]
|   │   └─ __init__().py
|   └─ after_pattern.drawio                 [UML Class Diagram]
| 
├─ tests/
│ ├─ __init__.py
│ ├─ test_game_time_before_pattern.py
│ ├─ test_game_time_after_pattern.py
│ ├─ test_combat_before_pattern.py
│ └─ test_combat_after_pattern.py
└─ README.md
```
---
- *model* -> code before applying pattern

---
## About
This is the source code for the python version of Zombie In My Pocket game

## Game Info
Imagine you're trapped in a spooky house full of zombies, and you need to save the world before midnight!

### The Goal
Find an evil zombie totem hidden in the house, then bury it in the graveyard before midnight - or you become zombie food!

### How to Play:

Explore the House: You start at the front door and flip over room tiles as you move through the house, discovering new rooms like kitchens, bedrooms, and basements.

Fight Zombies: Each room might have zombies in it. You can find weapons like "a machete, golf club, chain saw, or even your former uncle's grisly femur" to bash them.

Race Against Time: You must complete your mission before midnight - the game has a built-in time limit that makes every decision count.

Find the Temple: Look for the evil temple room where the cursed totem is hidden.

Bury the Totem: Once you have the totem, get to the backyard graveyard and bury it to win!

### Key Features:

It's a solo game that takes 5-20 minutes

Quick to play, easy to learn

It's a free print-and-play game you can download and make at home

Think of it like a mini horror movie where you're the hero trying to save the day - but you only have until midnight to do it!
