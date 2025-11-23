from src.model import GameTime

def test_initial_time_string():
    game_time = GameTime(9)
    assert str(game_time) == "The time is now 09:00PM"

def test_get_current_time():
    game_time = GameTime(10)
    assert game_time.get_current_time() == 10

def test_time_increase():
    game_time = GameTime(9)
    game_time.increase_time()
    assert game_time.get_current_time() == 10

def test_time_validity():
    game_time = GameTime(9, 12)
    assert game_time.is_time_valid() is True
    game_time._time = 12
    assert game_time.is_time_valid() is False

def test_am_pm_boundary():
    game_time = GameTime(12)
    assert "AM" in str(game_time)
    game_time._time = 11
    assert "AM" not in str(game_time)
