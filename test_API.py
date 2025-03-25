import allure
import pytest
from API.DeliveryAPI import DeliveryAPI

base_url = "https://market-delivery.yandex.ru/"
api = "api/"
ver = "v1/"
full = "full-text-search/"
menu_search = "/menu/search"

search_url = base_url+api+ver+menu_search
full_text_search_url = base_url + "eats/" + ver + full + ver + "/search"

med_deliveryapi = DeliveryAPI(search_url)


@allure.epic("Сайт Деливери")
@allure.severity("Hight")
@allure.story("POST запросы")
@allure.feature("Тестирование Поиска")
@allure.title("Поиск лекарства по полному названию  в магазине 'Аптека 36.6'")
@allure.description("Поисковая строка")
@allure.suite("Позитивные проверки")
def test_medicine_fullname_search_pozitive():
    medicine_fullname = med_deliveryapi.search_medicine_fullname("ацикловир")

    assert medicine_fullname.status_code == 200


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Позитивные проверки")
@allure.severity("Hight")
@allure.title("Поиск лекарства по части слова названия  в магазине 'Аптека 36.6'")
def test_part_medicine_name_search_pozitive():
    part_medicine_name = med_deliveryapi.search_part_medicine_name("ацик")
    assert part_medicine_name.status_code == 200


fullsearch_deliveryapi = DeliveryAPI(full_text_search_url)


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Позитивные проверки")
@allure.severity("Hight")
@allure.title("Поиск ресторана по полному названию в поисковой строке")
def test_search_restaurant_fullname_pozitive():
    restaurant_fullname = fullsearch_deliveryapi.search_restaurant_fullname("якитория")
    assert restaurant_fullname.status_code == 200


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Позитивные проверки")
@allure.severity("Hight")
@allure.title("Поиск ресторана по части названия в поисковой строке")
def test_search_part_restaurant_name_pozitive():
    part_restaurant_name = fullsearch_deliveryapi.search_part_restaurant_name("якит")
    assert part_restaurant_name.status_code == 200


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Позитивные проверки")
@allure.severity("Hight")
@allure.title("Поиск продукта по полному названию в поисковой строке")
def test_search_product_fullname_pozitive():
    product_fullname = fullsearch_deliveryapi.search_product_fullname("краб")
    assert product_fullname.status_code == 200


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Негативные проверки")
@allure.severity("Hight")
@allure.title("Поиск лекарства в поисковой строке без обязательного поля 'place_slug' в теле запроса")
def test_medicine_fullname_search_negative():
    medicine_fullname = med_deliveryapi.search_medicine_fullname_without_place_slug("ацикловир")
    assert medicine_fullname.status_code == 400
    assert medicine_fullname.json()["message"] == "Error at path 'place_slug': Field is missing"


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Негативные проверки")
@allure.severity("Hight")
@allure.title("Поиск продукта в поисковой строке без указания значения поля 'latitude' втеле запроса")
def test_search_product_fullname_negative_lat():
    product_fullname = fullsearch_deliveryapi.search_product_fullname_without_latitude("краб")
    assert product_fullname.status_code == 400
    assert product_fullname.json()["message"] == "Parse error at pos 113, path 'location.latitude': number was expected, but null found, the latest token was : null"


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.story("POST запросы")
@allure.suite("Негативные проверки")
@allure.severity("Hight")
@allure.title("Поиск продукта в поисковой строке без указания значения поля 'longitude' втеле запроса")
def test_search_product_fullname_negative_long():
    product_fullname = fullsearch_deliveryapi.search_product_fullname_without_longitude("краб")
    assert product_fullname.status_code == 400
    assert product_fullname.json()["message"] == "Parse error at pos 94, path 'location': missing required field 'longitude'"


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Негативные проверки")
@allure.severity("Hight")
@allure.title("Поиск продукта в поисковой строке без обязательного поля 'location' в теле запроса")
def test_search_product_fullname_negative_location():
    product_fullname = fullsearch_deliveryapi.search_product_fullname_without_location("краб")
    assert product_fullname.status_code == 400
    assert "Cannot use catalog search without location, 'location' or 'region_id' field must be provided" == product_fullname.json()["message"]


@allure.epic("Сайт Деливери")
@allure.feature("Тестирование Поиска")
@allure.story("POST запросы")
@allure.suite("Негативные проверки")
@allure.severity("Hight")
@allure.title("Поиск продукта в поисковой строке с несуществующими значениями системы координат в теле запроса")
@pytest.mark.xfail(reason="Баг API: Ошибка 500 вместо 400 при указании несуществующих координат.")
def test_search_product_fullname_wrong_coordinates():
    product_fullname = fullsearch_deliveryapi.search_product_fullname_wrong_coordinates("краб")
    assert product_fullname.status_code == 400
