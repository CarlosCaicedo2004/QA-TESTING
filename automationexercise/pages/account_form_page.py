from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AccountFormPage:
    PASSWORD = (By.ID, "password")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")            # VERIFICAR
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")    # VERIFICAR
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-qa='create-account']")  # VERIFICAR

    def __init__(self, driver):
        self.driver = driver

    def _type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def fill_account_details(self, password, first_name, last_name, address,
                             country, state, city, zipcode, mobile_number):
        self._type(self.PASSWORD, password)
        self._type(self.FIRST_NAME, first_name)
        self._type(self.LAST_NAME, last_name)
        self._type(self.ADDRESS, address)
        Select(self.driver.find_element(*self.COUNTRY)).select_by_visible_text(country)
        self._type(self.STATE, state)
        self._type(self.CITY, city)
        self._type(self.ZIPCODE, zipcode)
        self._type(self.MOBILE_NUMBER, mobile_number)

    def submit(self):
        button = self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()
