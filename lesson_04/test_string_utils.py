import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Проверки capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),  # Одно слово
    ("hello world", "Hello world"),  # Два слова через пробел
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),  # Цифры перед буквами в одной строке
    ("", ""),  # Пустая строка
    ("😀😂", "😀😂"),  # Строка смайликов
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


#  Проверки trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),  # Пробел в начале
    (" hello world", "hello world"),  # Пробел в начале и между словами
    ("python", "python"),  # Без пробела
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc ", "123abc "),  # Пробел после строки
    ("", ""),  # Пустая строка
    ("   ", ""),  # Строка из нескольких пробелов
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


#  Проверки contains
@pytest.mark.positive
@pytest.mark.parametrize("input_text, symbol", [
    ("Skypro", "r"),  # Символ в строке
    ("Teddy-bear", "-"),  # Спецсимвол в строке
])
def test_contains_positive(input_text, symbol):
    assert string_utils.contains(input_text, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("input_text, symbol", [
    ("Lesson 1", "2"),  # Неверный символ
    ("", "K"),  # Пустая строка, отсутствующий символ
    ("Lesson", "l")  # Неверный регистр
])
def test_contains_negative(input_text, symbol):
    assert string_utils.contains(input_text, symbol) is False


# Проверки delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "k", "SyPro"),  # Удаляем букву
    ("hello world", "l", "heo word"),  # Удаляем все 'l'
    ("12345", "2", "1345"),  # Удаляем цифру '2'
])
def test_delete_symbol_positive(input_string, symbol, expected_output):
    assert string_utils.delete_symbol(input_string, symbol) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "s", "SkyPro"),  # Удаляем букву другого регистра
    ("hello world", "5", "hello world"),  # Удаляем несуществующий символ
    ("", " ", ""),  # Удаляем пробел из пустой строки
])
def test_delete_symbol_negative(input_string, symbol, expected_output):
    assert string_utils.delete_symbol(input_string, symbol) == expected_output
