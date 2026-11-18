from selenium.webdriver.common.by import By


class CheckoutPage:
    NOMBRE = (By.ID, "first-name")
    APELLIDO = (By.ID, "last-name")
    CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUAR = (By.ID, "continue")
    BOTON_FINALIZAR = (By.ID, "finish")
    MENSAJE_FINAL = (By.CLASS_NAME, "complete-header")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def llenar_datos(self, nombre, apellido, codigo_postal):
        self.driver.find_element(*self.NOMBRE).send_keys(nombre)
        self.driver.find_element(*self.APELLIDO).send_keys(apellido)
        self.driver.find_element(*self.CODIGO_POSTAL).send_keys(codigo_postal)

    def continuar(self):
        self.driver.find_element(*self.BOTON_CONTINUAR).click()

    def finalizar(self):
        self.driver.find_element(*self.BOTON_FINALIZAR).click()

    def obtener_mensaje_final(self):
        return self.driver.find_element(*self.MENSAJE_FINAL).text

    def obtener_error(self):
        return self.driver.find_element(*self.ERROR).text