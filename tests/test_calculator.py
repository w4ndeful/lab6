"""Тести для модуля calculator."""

import pytest
from calculator import add, subtract, multiply, divide


class TestCalculator:
    """Тести для функцій калькулятора."""

    def test_add(self):
        """Тест додавання."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_subtract(self):
        """Тест віднімання."""
        assert subtract(5, 2) == 3
        assert subtract(0, 5) == -5

    def test_multiply(self):
        """Тест множення."""
        assert multiply(4, 5) == 20
        assert multiply(0, 100) == 0

    def test_divide(self):
        """Тест ділення."""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Тест ділення на нуль."""
        with pytest.raises(ValueError):
            divide(10, 0)
