from .test_base import BaseTestCalculator

class TestBasicOperations(BaseTestCalculator):
    def test_add(self):
        assert self.calc.add(2, 3) == 5

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2


class TestAdvancedOperations(BaseTestCalculator):
    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        import pytest
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)
