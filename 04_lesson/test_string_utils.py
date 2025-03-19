import pytest

from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("солнце", "Солнце"), #делает первую букву заглавной, текст кириллицей
    ("солнце светит", "Солнце светит"), #делает заглавной букву в первом слове
    ("python123", "Python123"), #делает первую букву заглавной, текст латиницей
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"), #цифры в начале строки не подвергаются изменениям
    ("", ""), #пустой текст
    ("   ", "   "), #строка из пробелов
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" мир", "мир"), #пробел в начале строки исчез
    (" 1000 и одна ночь", "1000 и одна ночь"), #пробел исчез только в начале строки
    ("   великолепно  ", "великолепно  "), #несколько пробелов в начале строки исчезли
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Тест", "Т", True),
    ("123", "1", True),
    ("из-за", "-", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "ю", False),
    ("Juli", "j", False),
    ("123", "5", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Тест", "Т", "ест"),
    ("123", "1", "23"),
    ("из-за", "-", "изза"),
    ("тест не пройден", "не", "тест  пройден")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Тест", "", "Тест"),
    ("", "", ""),
    ("   ", "", "   ")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected