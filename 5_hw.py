from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def check_element():
    """Переходит на страницу saucedemo.com и проверяет наличие заданных полей"""
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        wait = WebDriverWait(driver, 10)

        # поиск элементов
        icon_user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
        icon_password = driver.find_element(By.CSS_SELECTOR, '#password')
        button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')


        print('Элементы найдены' if icon_user_name and icon_password and button_login else 'Элементы не найдены')
    except NoSuchElementException as exc:
        print(exc)


check_element()