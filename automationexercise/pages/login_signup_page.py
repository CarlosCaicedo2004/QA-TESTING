from selenium.webdriver.common.by import By

URL = "https://automationexercise.com/login"


class LoginSignupPage:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa='login-button']")
    SIGNUP_NAME = (By.CSS_SELECTOR, "[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "[data-qa='signup-button']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URL)

    def start_signup(self, name, email):
        self.driver.find_element(*self.SIGNUP_NAME).send_keys(name)
        self.driver.find_element(*self.SIGNUP_EMAIL).send_keys(email)
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def login(self, email, password):
        self.driver.find_element(*self.LOGIN_EMAIL).send_keys(email)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
