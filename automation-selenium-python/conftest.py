import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture
def driver_logueado(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver
