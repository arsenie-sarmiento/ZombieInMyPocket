import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model.calculator import calculator
from src.model import calculator

def test_add():
    assert calculator(2, 3) == 5
    assert calculator(-1, 1) == 0
