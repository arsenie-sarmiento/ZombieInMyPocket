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

