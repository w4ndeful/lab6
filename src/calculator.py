"""Простий калькулятор для демонстрації тестів."""

def add(a, b):
    """Додавання двох чисел."""
    return a + b


def subtract(a, b):
    """Віднімання двох чисел."""
    return a - b


def multiply(a, b):
    """Множення двох чисел."""
    return a * b


def divide(a, b):
    """Ділення двох чисел."""
    if b == 0:
        raise ValueError("Ділення на нуль не дозволено!")
    return a / b
