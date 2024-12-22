import pytest
from unittest.mock import patch
import math

# Импортируем функции из вашего модуля (предположим, что он называется `math_operations`)
from LR5 import basic_operations, factorial, square_root, solve_quadratic

# Тесты для базовых операций
def test_basic_operations():
    result = basic_operations(10, 5)
    assert result["Сложение"] == 15
    assert result["Вычитание"] == 5
    assert result["Умножение"] == 50
    assert result["Деление"] == 2

def test_basic_operations_division_by_zero():
    result = basic_operations(10, 0)
    assert result["Деление"] == "Деление на ноль невозможно"

# Тесты для факториала
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == "Факториал отрицательного числа не определен"

# Тесты для квадратного корня
def test_square_root():
    assert square_root(16) == 4
    assert square_root(0) == 0
    assert square_root(-16) == "Квадратный корень отрицательного числа не определен"

# Тесты для решения квадратного уравнения
def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)
    assert solve_quadratic(1, 2, 1) == (-1.0,)
    assert solve_quadratic(1, 0, 1) == "Нет действительных корней"

# Параметризованный тест для проверки квадратного уравнения
@pytest.mark.parametrize("a, b, c, expected", [
    (1, -3, 2, (2.0, 1.0)),
    (1, 2, 1, (-1.0,)),
    (1, 0, 1, "Нет действительных корней"),
    (0, 2, 1, "Это не квадратное уравнение"),
])
def test_parametrized_solve_quadratic(a, b, c, expected):
    assert solve_quadratic(a, b, c) == expected

# Тест с использованием мока
@patch('math.sqrt', return_value=3)
def test_square_root_mocked(mock_sqrt):
    assert square_root(9) == 3
    mock_sqrt.assert_called_once_with(9)

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
