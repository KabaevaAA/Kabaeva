import math


def basic_operations(a, b):
    """Выполняет базовые математические операции."""
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Деление на ноль невозможно"

    return {
        "Сложение": addition,
        "Вычитание": subtraction,
        "Умножение": multiplication,
        "Деление": division
    }


def factorial(n):
    """Вычисляет факториал числа n."""
    if n < 0:
        return "Факториал отрицательного числа не определен"
    return math.factorial(n)


def square_root(n):
    """Вычисляет квадратный корень числа n."""
    if n < 0:
        return "Квадратный корень отрицательного числа не определен"
    return math.sqrt(n)


def solve_quadratic(a, b, c):
    """Решает квадратное уравнение ax^2 + bx + c = 0."""
    if a == 0:
        return "Это не квадратное уравнение"

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        return "Нет действительных корней"


# Примеры использования функций
if __name__ == "__main__":
    a = 10
    b = 5

    print("Базовые операции:", basic_operations(a, b))
    print("Факториал числа 5:", factorial(5))
    print("Квадратный корень числа 16:", square_root(16))
    print("Корни квадратного уравнения 2x^2 + 4x + 2:", solve_quadratic(2, 4, 2))