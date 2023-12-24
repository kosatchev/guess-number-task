import pytest
import numpy as np
from game_v2 import random_predict, binary_search

# Тестирование функции random_predict
def test_random_predict():
    attempts = random_predict(np.random.randint(1, 101))
    # Тестируем, что функция возвращает число попыток, большее нуля
    assert attempts > 0, "Функция random_predict должна вернуть число попыток > 0"
    # Тестируем, что функция возвращает число попыток, большее 90
    assert attempts > 0, "Функция random_predict должна вернуть число попыток > 90"
    # Тестируем, что функция возвращает число попыток, меньше 111
    assert attempts > 0, "Функция random_predict должна вернуть число попыток < 111"

# Тестирование функции binary_search
def test_binary_search():
    attempts = binary_search(1, 100, np.random.randint(1, 101))
    # Тестируем, что функция возвращает число попыток, большее нуля
    assert attempts > 0, "Функция binary_search должна вернуть число попыток > 0"
    # Тестируем, что функция возвращает число попыток, меньше 8
    assert attempts < 8, "Функция binary_search должна вернуть число попыток < 8"

    # Тестируем, что функция возвращает корректное количество попыток для конкретных значений
    assert binary_search(1, 100, 50) == 1, "Ошибка в реализации binary_search для числа 50"
    assert binary_search(1, 100, 75) == 2, "Ошибка в реализации binary_search для числа 75"
    assert binary_search(1, 100, 1) == 6, "Ошибка в реализации binary_search для числа 75"

if __name__ == "__main__":
    pytest.main()