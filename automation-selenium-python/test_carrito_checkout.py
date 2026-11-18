from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

MOCHILA = "sauce-labs-backpack"


def test_tc013_agregar_producto(driver_logueado):
    inventario = InventoryPage(driver_logueado)
    inventario.agregar_producto(MOCHILA)
    assert inventario.obtener_contador() == "1"


def test_tc015_quitar_producto(driver_logueado):
    inventario = InventoryPage(driver_logueado)
    inventario.agregar_producto(MOCHILA)
    inventario.quitar_producto(MOCHILA)
    assert inventario.obtener_contador() == "0"


def test_tc019_checkout_exitoso(driver_logueado):
    InventoryPage(driver_logueado).agregar_producto(MOCHILA)
    InventoryPage(driver_logueado).ir_al_carrito()
    CartPage(driver_logueado).ir_a_checkout()
    checkout = CheckoutPage(driver_logueado)
    checkout.llenar_datos("Juan", "Perez", "110111")
    checkout.continuar()
    checkout.finalizar()
    assert "Thank you for your order" in checkout.obtener_mensaje_final()


def test_tc020_checkout_sin_nombre(driver_logueado):
    InventoryPage(driver_logueado).agregar_producto(MOCHILA)
    InventoryPage(driver_logueado).ir_al_carrito()
    CartPage(driver_logueado).ir_a_checkout()
    checkout = CheckoutPage(driver_logueado)
    checkout.llenar_datos("", "Perez", "110111")
    checkout.continuar()
    assert "First Name is required" in checkout.obtener_error()