"""Головний модуль застосунку."""

from calculator import add, subtract, multiply, divide


def main():
    """Основна функція."""
    print("Калькулятор запущений!")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print(f"10 / 2 = {divide(10, 2)}")


if __name__ == "__main__":
    main()
