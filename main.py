import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.www.oma.by
        driver.get("https://www.oma.by//")
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы (строка поиска)
        elem = driver.find_element(By.XPATH, "//div[@class='one-row-form_input-cell']")

        #нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        elem = driver.find_element(By.XPATH, "//input[@ name = 'q']")
        # ждем 5 секунд
        elem.send_keys("chupakabra")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        #elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        # проверка наличия строки "Nичего не найдено по запросу «chupakabra»"
        # на странице с результатами поиска
        self.assertIn("0 товаров", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q
        # на обновленной странице

        # нажатие на ссылку
        elem = driver.find_element(By.XPATH, "//input[@ name = 'q']")
        #elem = driver.find_element(By.XPATH, "//div[@class='search-form_row-input']")
        # очищаем строку поиска
        elem.clear()
        # ждем 5 секунд
        time.sleep(5)
        # набор слова pycon в найденном элементе
        elem.send_keys("pycon")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        #elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия строки "No results found."
        # на странице с результатами поиска
        #self.assertIn("No results found.", driver.page_source)



    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
