from selenium.webdriver.common.by import By


def test_tc013_agregar_producto(driver_logueado):
    driver = driver_logueado
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1"


def test_tc015_quitar_producto(driver_logueado):
    driver = driver_logueado
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    contadores = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(contadores) == 0


def test_tc019_checkout_exitoso(driver_logueado):
    driver = driver_logueado
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("110111")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    mensaje = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order" in mensaje


def test_tc020_checkout_sin_nombre(driver_logueado):
    driver = driver_logueado
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("110111")
    driver.find_element(By.ID, "continue").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "First Name is required" in error
