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
        
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_login_logout(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.www.oma.by
        # на которой есть кнопка Вход или
        driver.get("https://www.oma.by//")
        # ждем 5 секунд
        time.sleep(5)
        # поиск ссылки с текстом "Вход или"//span[@class='complex-link_top-txt']
        elem = driver.find_element(By.XPATH, "//span[@class='complex-link_top-txt']")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='login')
        elem = driver.find_element(By.XPATH, "//input[@name='PHONE']")
        # ввод логина
        elem.send_keys("445548956")
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='password')
        elem = driver.find_element(By.XPATH, "//input[@name='PASSWORD']")
        # ввод логина
        elem.send_keys("1b60b459")
        # ждем 5 секунд
        time.sleep(5)
        click = driver.find_element(By.XPATH, "//span[@class='checkbox-visual']")
        driver.execute_script("arguments[0].click();", click)
        time.sleep(5)
        elem = driver.find_element(By.XPATH, "//div[@class='btns__block']/button[1]")
        #driver.execute_script("arguments[0].click();", elem)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия на странице строки "Мой кабинет"
        # после входа
        self.assertIn("Мой кабинет", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # вывод кода страницы для отладки, потом можно будет убрать
        print(driver.page_source)
        # поиск ссылки с текстом "Выход"
        elem = driver.find_element(By.XPATH, "//a[@class ='item_link'][contains(text(), 'Выйти')]")
        # нажатие на кнопку
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    def test_about_list(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.oma.by
        driver.get("http://www.oma.by")
        # получаем список ссылок в меню ВЕСЬ КАТАЛОГ
        elem = driver.find_element(By.XPATH, "//span[@class = 'catalog-btn_text'][contains(text(), 'Весь каталог')]")

        elem.click()
        time.sleep(3)
        # получаем список всех дверей

        elem = driver.find_element(By.XPATH, "// a[ @ href = '/dveri-c']")
        # driver.execute_script("arguments[0].click();", elem)
        elem.click()
        time.sleep(5)
        # получаем конкретную дверь
        elem = driver.find_element(By.XPATH, "// a[@href = '/dvernoe-polotno-bona-01-listvennitsa-sibiu-200-80-2-280878-p']")
        driver.execute_script("arguments[0].click();", elem)

        # добавляем дверь в карзину
        elem = driver.find_elements(By.XPATH, "//button[@class = 'btn'][contains(text(), 'Корзина')]")


        elem.click()
        time.sleep(5)



if __name__ == '__main__':
    unittest.main()
