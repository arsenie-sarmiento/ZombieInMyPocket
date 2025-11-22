from src.model.calculator import Calculator

class BaseTestCalculator:
    """Base test class with shared setup."""
    def setup_method(self):
        self.calc = Calculator()
