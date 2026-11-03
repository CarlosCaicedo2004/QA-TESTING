from selenium.webdriver.common.by import By


def hacer_login(driver, usuario, contrasena):
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(contrasena)
    driver.find_element(By.ID, "login-button").click()


def test_tc001_login_exitoso(driver):
    hacer_login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_tc002_usuario_bloqueado(driver):
    hacer_login(driver, "locked_out_user", "secret_sauce")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked out" in error


def test_tc003_contrasena_incorrecta(driver):
    hacer_login(driver, "standard_user", "wrong_password")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "do not match" in error
