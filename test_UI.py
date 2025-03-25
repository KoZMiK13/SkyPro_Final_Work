from Pages.MainPage import MainPage
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

pozitive_search_list = [
        ("Здрасте", "Здрасте"),
        ("Subway", "Subway"),
        ("па, Шоколад молочный Milka с дробленым фундуком", "па, Шоколад молочный Milka с дробленым фундуком"),
        ("Молоко 3.2%", "Молоко 3.2%"),
        ("Evervess Cola/Эвервесс Кола газированный напиток 1л, бутылка", "Evervess Cola/Эвервесс Кола газированный напиток 1л, бутылка"),
        ("молоко питьевое, Молоко питьевое ультрапастеризованное", "молоко питьевое, Молоко питьевое ультрапастеризованное"),
        ("Lounge-bar №1, Хот-дог-очень остро", "Lounge-bar №1, Хот-дог-очень остро"),
        ("вода питьевая", "вода питьевая"),
        ("ШАУРМА", "ШАУРМА"),
        ("Крабовые палочки", "Крабовые палочки"),
        ("  роллы", "  роллы"),
        ("папа Джонс  ", "папа Джонс  "),
        ("Бургер King", "Бургер King"),
        ("Якитория", "Якитория"),
        ("якит", "якит")
        ]

negative_search_list = [
    ("", ""),
    ("    ", "    "),
    ("а, !, l", "а, !, l"),
    ("<p1>бумажные полотенца/<p1>", "<p1>бумажные полотенца/<p1>"),
    ('😀', '😀'),
    ("аоеиюя", "аоеиюя"),
    ("прлдстб", "прлдстб"),
    ("ぼぼ", "ぼぼ"),
    ("درس", "درس"),
    ("www.mail.ru", "www.mail.ru")
    ]


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("UI тесты")
@allure.suite("Позитивные проверки")
@allure.severity("Hight")
@allure.title("Проверка строки поиска")
@pytest.mark.parametrize("query, res", pozitive_search_list)
def test_search_field_pozitive(query, res):

    mainpage = MainPage(browser)
    mainpage.search_field(query)

    query = mainpage.text_in_search_field_before_search()
    mainpage.click_search_button()
    res = mainpage.text_in_search_field_after_search()
    with allure.step("Подтверждение что текст в поле ввода до поиска {query} соответствует тексту после поиска {res}"):
        assert query == res


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("UI тесты")
@allure.suite("Негативные проверки")
@allure.severity("Hight")
@allure.title("Проверка строки поиска")
@pytest.mark.parametrize("query, res", negative_search_list)
def test_search_field_negative(query, res):

    mainpage = MainPage(browser)
    mainpage.search_field(query)
    query = mainpage.text_in_search_field_before_search()
    mainpage.click_search_button()
    res = mainpage.text_in_search_field_after_search()
    with allure.step("Подтверждение что текст в поле ввода до поиска {query} соответствует тексту после поиска {res}"):
        assert query == res
