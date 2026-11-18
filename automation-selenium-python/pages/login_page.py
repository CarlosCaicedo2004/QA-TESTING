from selenium.webdriver.common.by import By


class LoginPage:
    USUARIO = (By.ID, "user-name")
    CONTRASENA = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, usuario, contrasena):
        self.driver.find_element(*self.USUARIO).send_keys(usuario)
        self.driver.find_element(*self.CONTRASENA).send_keys(contrasena)
        self.driver.find_element(*self.BOTON_LOGIN).click()

    def obtener_error(self):
        return self.driver.find_element(*self.ERROR).text