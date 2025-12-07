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
### Testimg

[Python Test Explorer](https://www.youtube.com/watch?v=V-1Sgv3xaaI&t=4s)

1. Setup
```
pip install coverage
coverage --version

pip install pytest pytest-cov
pytest --cov=your_package

coverage html
```

2. Run test
```
coverage run --branch -m pytest .\tests\test_combat_before_pattern.py -vvv
coverage run --branch -m pytest .\tests\test_combat_after_pattern.py -vvv

coverage run --branch -m pytest .\tests\test_player_before_pattern.py -vvv
coverage run --branch -m pytest .\tests\test_player_after_pattern.py -vvv

coverage html
coverage report -m

```


---
### File Structure
```
ZombieInMyPocket/
├─ .gitignore
├─ src/
│ ├─ __init__.py                            [empty]
│ ├─ model/
│ │ ├─ game_pieces/                           
| │ │ ├─ __init__.py
| │ │ ├─ board.py
| │ │ ├─ dev_card.py
│ | │ └─ game_pieces.py                     [target block's component]
│ │ ├─ combat/                              
| │ │ ├─ __init__.py
│ | │ └─ combat.py                          [target block's component]
│ | └─ ... (other model files)
│ │ ├─ interfaces/
| │ │ ├─ __init__.py
| │ │ ├─ i_combat.py
| │ │ ├─ i_game_pieces.py
| │ │ ├─ i_dev_card.py
| │ │ ├─ i_tile.py
| │ │ └─ ... (other interface files)
│ │ |
│ │ ├─ __init__.py
| │ └─ before_pattern.drawio                [UML Class Diagram]
| |
│ └─ model_after_pattern/                   [refactored]
│   ├─ enums/
|   │   ├─ combat_option.py
|   │   └─ __init__().py
│   ├─ interfaces/
|   │   ├─ combat_strategy.py                   [Strategy]
|   │   ├─ i_game_pieces.py                     [Client Interface/Abstract Client]
|   │   ├─ i_game_pieces_factory.py             [Abstract Factory]
|   │   ├─ i_board.py                           [Abstract Product]
|   │   ├─ i_dev_card.py                        [Abstract Product]
|   │   ├─ i_tile.py                            [Abstract Product]
|   │   └─ __init__().py
│   ├─ game_pieces/
|   │   ├─ game_pieces.py                      [Client]
|   │   ├─ default_game_pieces_factory.py      [Concrete Factory]
|   │   ├─ dev_card.py                         [Concrete Product]
|   │   ├─ board.py                            [Concrete Product]
|   │   ├─ tile.py                             [Concrete Product]
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
│ ├─ mocks/                                 [Mock files]
| │   ├─ __init__.py                        
| │   ├─ combat.py                          
| │   ├─ player.py                          
| │   ├─ strategy.py                        
| │   └─ game_pieces_factory.py                        
│ ├─ __init__.py
│ ├─ test_game_pieces_before_pattern.py
│ ├─ test_game_pieces_after_pattern.py
│ ├─ test_combat_before_pattern.py
│ └─ test_combat_after_pattern.py
└─ README.md
```
---
- *model* -> code before applying pattern

