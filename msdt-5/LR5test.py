import pytest
from unittest.mock import patch
from LR5 import basic_operations, factorial, square_root, \
    solve_quadratic


def test_basic_operations():
    """Тестирует базовые математические операции."""
    assert basic_operations(10, 5) == {
        "Сложение": 15,
        "Вычитание": 5,
        "Умножение": 50,
        "Деление": 2.0
    }

    assert basic_operations(10, 0) == {
        "Сложение": 10,
        "Вычитание": 10,
        "Умножение": 0,
        "Деление": "Деление на ноль невозможно"
    }


def test_factorial():
    """Тестирует функцию факториала."""
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == "Факториал отрицательного числа не определен"


def test_square_root():
    """Тестирует функцию квадратного корня."""
    assert square_root(16) == 4
    assert square_root(0) == 0
    assert square_root(-1) == "Квадратный корень отрицательного числа не определен"


def test_solve_quadratic():
    """Тестирует решение квадратного уравнения."""
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)  # Два действительных корня
    assert solve_quadratic(1, 2, 1) == (-1.0,)  # Один действительный корень
    assert solve_quadratic(1, 0, 1) == "Нет действительных корней"  # Нет действительных корней
    assert solve_quadratic(0, 2, 1) == "Это не квадратное уравнение"  # Не квадратное уравнение


# Параметризованный тест для проверки различных значений факториала
@pytest.mark.parametrize("input_value, expected_output", [
    (5, 120),
    (3, 6),
    (4, 24),
    (6, 720),
    (0, 1),
])
def test_factorial_parametrized(input_value, expected_output):
    """Параметризованный тест для функции факториала."""
    assert factorial(input_value) == expected_output


# Параметризованный тест для проверки различных значений квадратного корня
@pytest.mark.parametrize("input_value, expected_output", [
    (16, 4),
    (25, 5),
    (0, 0),
    (-1, "Квадратный корень отрицательного числа не определен"),
])
def test_square_root_parametrized(input_value, expected_output):
    """Параметризованный тест для функции квадратного корня."""
    assert square_root(input_value) == expected_output


# Тест с использованием мока для проверки вывода функции
@patch('builtins.print')
def test_basic_operations_mock(mock_print):
    """Тестирует базовые операции с использованием мока."""
    basic_operations(10, 5)
    mock_print.assert_not_called()  # Проверяет, что print не был вызван
