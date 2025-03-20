import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        # Переход на страницу доставки Яндекс.Маркета
        driver.get(
            "https://market-delivery.yandex.ru/spb?shippingType=delivery"
                )

    @allure.step("Поиск, выбор и очистка поля поиска с ожиданием полной загрузки, ввод текста {query}")
    def search_field(self, query: str):
        """
        Поиск поля ввода и ввод запроса
        """
        search_field = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id_1"))
        )

        search_field.clear()  # Очистка поля ввода

        search_field.send_keys(query)  # Ввод запроса

    @allure.step("Получение текста из строки поиска до нажатия на поиск")
    def text_in_search_field_before_search(self):
        search_field_before_search = self._driver.find_element(
            By.CSS_SELECTOR, "input#id_1").text
        return search_field_before_search

    @allure.step("Нажатие на кнопку поиска")
    def click_search_button(self):
        # Нажатие на кнопку поиска
        search_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/div/header/div/div[1]/div/div[1]/div/div/div[3]/div/button")
            )
        )

        search_button.click()  # Клик по кнопке

    @allure.step("Нажать кнопку 'Войти'")
    def enter_telephone_number(self):
        # Нажатие на кнопку входа
        enter_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.DesktopUIButton_root"))
        )
        enter_button.click()  # Клик по кнопке входа

        # Клик по кнопке "Войти"
        sign_in_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#passp:sign-in"))
        )
        sign_in_button.click()  # Клик по кнопке "Войти"

    @allure.step("Получение текста из строки поиска После нажатия на поиск")
    def text_in_search_field_after_search(self):
        search_field_after_search = self._driver.find_element(By.CSS_SELECTOR, "input#id_2").text
        return search_field_after_search
