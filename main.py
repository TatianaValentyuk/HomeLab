import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By




class Kalkpro(unittest.TestCase):

    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_about_breadcrumbs(self):
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

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
