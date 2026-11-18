from selenium.webdriver.common.by import By


class InventoryPage:
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    CONTADOR = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def agregar_producto(self, producto):
        self.driver.find_element(By.ID, f"add-to-cart-{producto}").click()

    def quitar_producto(self, producto):
        self.driver.find_element(By.ID, f"remove-{producto}").click()

    def obtener_contador(self):
        elementos = self.driver.find_elements(*self.CONTADOR)
        return elementos[0].text if elementos else "0"

    def ir_al_carrito(self):
        self.driver.find_element(*self.CARRITO).click()