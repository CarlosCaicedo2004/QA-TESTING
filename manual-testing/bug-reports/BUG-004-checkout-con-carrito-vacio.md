# BUG-004: Se puede continuar el pago con el carrito vacío

## Resumen
La aplicación permite iniciar y completar el proceso de checkout aunque el carrito no tenga ningún producto.

## Entorno
- **URL:** https://www.saucedemo.com
- **Navegador:** Chrome
- **Usuario:** standard_user

## Pasos para reproducir
1. Iniciar sesión con standard_user / secret_sauce
2. Verificar que el carrito esté vacío
3. Click en el ícono del carrito y luego en Checkout
4. Completar nombre, apellido y código postal
5. Click en Continue y luego en Finish

## Resultado actual
La orden se completa con éxito aunque el carrito no tiene productos.

## Resultado esperado
El sistema no debe permitir avanzar con el carrito vacío: el botón Checkout debería estar deshabilitado o mostrar un mensaje indicando que el carrito está vacío.

## Impacto
Se podrían generar órdenes sin productos, con totales en cero.

## Severidad / Prioridad
- **Severidad:** Alta
- **Prioridad:** Alta

## Evidencia
[Captura de la pantalla final de confirmación con el carrito vacío]

## Notas
Relacionado con TC-017 y TC-019.
