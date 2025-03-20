import allure
import requests


class DeliveryAPI:
    """Класс для работы с API"""
    def __init__(self, url):
        self.url = url

    @allure.step("POST запрос для поиска лекарства по полному названию {medicine} в магазине 'Аптека 36.6'")
    def search_medicine_fullname(self, medicine: str):
        """"
        Поиск лекарства по полному названию в магазине 'Аптека 36.6'
        """
        body = {
            "region_id": 1,
            "place_slug": "apteka_366_direct_pbjfn",
            "text": medicine,
            "location": {
                "lat": 55.43923682107633,
                "lon": 37.75256219779564
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(
            self.url, headers=headers, json=body
            )

    @allure.step("POST запрос для поиска лекарства по части слова {part_medicine} в магазине 'Аптека 36.6'")
    def search_part_medicine_name(
            self, part_medicine: str):
        """
        Поиск лекарства по части слова названия в магазине 'Аптека 36.6'
        """
        body = {
            "region_id": 1,
            "place_slug": "apteka_366_direct_pbjfn",
            "text": part_medicine,
            "location": {
                "lat": 55.43923682107633,
                "lon": 37.75256219779564
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(
            self.url, headers=headers, json=body
            )

    @allure.step("POST запрос для поиска ресторана по полному названию {restaurant} в поисковой строке")
    def search_restaurant_fullname(self, restaurant: str):
        """
        Поиск ресторана по полному названию в поисковой строке
        """
        body = {
            "text": restaurant,
            "filters": [],
            "location": {
                "longitude": 37.75256219779564,
                "latitude": 55.43923682107633
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(self.url, headers=headers, json=body)

    @allure.step("POST запрос для поиска ресторана по части названия {part_restaurant}")
    def search_part_restaurant_name(self, part_restaurant: str):
        """
        Поиск ресторана по части названия в поисковой строке
        """
        body = {
            "text": part_restaurant,
            "filters": [],
            "location": {
                "longitude": 37.75256219779564,
                "latitude": 55.43923682107633
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(self.url, headers=headers, json=body)

    @allure.step("POST запрос для поиска продукта по полному наименованиюв {prod_name} поисковой строке")
    def search_product_fullname(self, prod_name: str):
        """
        Поиск продукта по полному названию в поисковой строке
        """
        body = {
            "text": prod_name,
            "filters": [],
            "location": {
                "longitude": 37.75256219779564,
                "latitude": 55.43923682107633
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(self.url, headers=headers, json=body)

    @allure.step("POST запрос без обязательного поля 'place_slug' {place_slug} в теле запроса")
    def search_medicine_fullname_without_place_slug(self, medicine: str, place_slug=None):
        """
        Поиск лекарства в поисковой строке без обязательного поля 'place_slug' в теле запроса
        """
        body = {
            "region_id": 1,
            "place_slug": place_slug,
            "text": medicine,
            "location": {
                "lat": 55.43923682107633,
                "lon": 37.75256219779564
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(
            self.url, headers=headers, json=body
            )

    @allure.step('POST запрос без указания значения поля "latitude" {lat} в теле запроса')
    def search_product_fullname_without_latitude(self, prod_name: str, lat=None):
        """
        Поиск продукта в поисковой строке без указания значения поля "latitude" в теле запроса
        """
        body = {
            "text": prod_name,
            "filters": [],
            "location": {
                "longitude": 37.75256219779564,
                "latitude": lat
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(self.url, headers=headers, json=body)

    @allure.step('POST запрос без указания значения поля "longitude" в теле запроса')
    def search_product_fullname_without_longitude(self, prod_name: str, long=None):
        """Поиск продукта в поисковой строке без указания значения поля "longitude" в теле запроса"""
        body = {
            "text": prod_name,
            "filters": [],
            "location": {
                "longitude": long,
                "latitude": 55.43923682107633
                }
            }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(self.url, headers=headers, json=body)

    @allure.step('POST запрс без обязательного поля "location" в теле запроса')
    def search_product_fullname_without_location(self, prod_name: str):
        """Поиск продукта  в поисковой строке без обязательного поля "location" в теле запроса"""
        body = {
            "text": prod_name,
            "filters": []
        }

        headers = {
            "Content-Type": "application/json"
        }

        return requests.post(self.url, headers=headers, json=body)

    @allure.step('POST запрос с несуществующими значениями системы координат в теле запроса')
    def search_product_fullname_wrong_coordinates(self, prod_name: str):
        """Поиск продукта в поисковой строке с несуществующими значениями системы координат в теле запроса"""
        body = {
            "text": prod_name,
            "filters": [],
            "location": {
                "longitude": 190,
                "latitude": -190
            }
        }

        headers = {
            "Content-Type": "application/json"
            }

        return requests.post(self.url, headers=headers, json=body)
