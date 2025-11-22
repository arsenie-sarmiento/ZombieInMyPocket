from src.model_after_pattern import GameTime, TimeFormatter, GameTimeDisplay


def test_display_uses_formatter():
    gt = GameTime(9)
    display = GameTimeDisplay(gt, TimeFormatter())
    assert str(display) == "The time is now 09:00AM"

def test_am_pm_boundary_corrected():
    gt = GameTime(11)
    display = GameTimeDisplay(gt, TimeFormatter())
    assert "AM" in str(display)

    gt2 = GameTime(15)
    display2 = GameTimeDisplay(gt2, TimeFormatter())
    assert "PM" in str(display2)

def test_time_increase_does_not_affect_formatting_logic():
    gt = GameTime(10)
    display = GameTimeDisplay(gt, TimeFormatter())
    gt.increase_hour()
    assert str(display) == "The time is now 11:00AM"

# def test_custom_formatter_can_be_injected():
#     gt = GameTime(14)
#     display = GameTimeDisplay(gt, MilitaryFormatter())
#     assert str(display) == "The time is now 14:00"

def test_display_with_fake_time_mock():
    class FakeTime:
        def __init__(self, hour): self._hour = hour
        def get_hour(self): return self._hour
    fake = FakeTime(5)
    display = GameTimeDisplay(fake, TimeFormatter())
    assert str(display) == "The time is now 05:00AM"
