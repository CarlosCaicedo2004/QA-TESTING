from selenium.webdriver.common.by import By


class CartPage:
    BOTON_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def ir_a_checkout(self):
        self.driver.find_element(*self.BOTON_CHECKOUT).click()