from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestMandatoryForms(unittest.TestCase):
    def test_m_forms1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first:required")
        element1.send_keys("First Name")

        element2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second:required")
        element2.send_keys("Last name")

        element3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third:required")
        element3.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_m_forms2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first:required")
        element1.send_keys("First Name")

        element2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second:required")
        element2.send_keys("Last name")

        element3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third:required")
        element3.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()