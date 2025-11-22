from src.model.game_time.game_time import GameTime

def test_initial_time_string():
    g = GameTime(9)
    # original __str__ method embedded in GameTime
    assert str(g) == "The time is now 09:00AM"

def test_get_current_time():
    g = GameTime(10)
    assert g.get_current_time() == 10

def test_time_increase():
    g = GameTime(9)
    g.increase_time()
    assert g.get_current_time() == 10

def test_time_validity():
    g = GameTime(9, 12)
    assert g.is_time_valid() is True
    g._time = 12
    assert g.is_time_valid() is False

def test_am_pm_boundary():
    g = GameTime(12)
    assert "AM" in str(g)
    g._time = 11
    assert "AM" not in str(g)  # matches old behavior
