# BUG-006: El campo de código postal acepta letras

## Resumen
En el formulario de checkout, el campo Zip/Postal Code permite escribir letras y no valida el formato.

## Entorno
- **URL:** https://www.saucedemo.com
- **Navegador:** Chrome
- **Usuario:** standard_user

## Pasos para reproducir
1. Iniciar sesión con standard_user / secret_sauce
2. Agregar un producto al carrito
3. Ir al carrito y click en Checkout
4. En Zip/Postal Code escribir "abcde"
5. Completar los demás campos y click en Continue

## Resultado actual
El campo acepta las letras. [Completar: ¿el sistema te dejó continuar con ese valor?]

## Resultado esperado
El campo debería aceptar solo un formato válido de código postal o mostrar un mensaje de error.

## Impacto
Se pueden registrar datos de envío inválidos.

## Severidad / Prioridad
- **Severidad:** Media
- **Prioridad:** Media

## Evidencia
[Captura del campo con letras]

## Notas
Relacionado con TC-022 y TC-019.
