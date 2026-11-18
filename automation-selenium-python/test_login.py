from pages.login_page import LoginPage


def test_tc001_login_exitoso(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_tc002_usuario_bloqueado(driver):
    pagina = LoginPage(driver)
    pagina.login("locked_out_user", "secret_sauce")
    assert "locked out" in pagina.obtener_error()


def test_tc003_contrasena_incorrecta(driver):
    pagina = LoginPage(driver)
    pagina.login("standard_user", "wrong_password")
    assert "do not match" in pagina.obtener_error()