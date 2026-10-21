# BUG-001: Imágenes de productos incorrectas al usar problem_user

## Resumen
Al iniciar sesión con `problem_user`, las imágenes de los productos no corresponden a los artículos reales; todas muestran la misma imagen (un perro).

## Entorno
- **URL:** https://www.saucedemo.com
- **Navegador:** Chrome (última versión estable)
- **Usuario:** problem_user / secret_sauce

## Pasos para reproducir
1. Ir a https://www.saucedemo.com
2. Iniciar sesión con `problem_user` / `secret_sauce`
3. Observar las imágenes en la página de inventario

## Resultado actual
Todas las tarjetas de producto muestran la misma imagen, sin importar el producto.

## Resultado esperado
Cada producto muestra su imagen correspondiente, como ocurre con `standard_user`.

## Severidad / Prioridad
- **Severidad:** Media (afecta la experiencia visual, no bloquea la funcionalidad)
- **Prioridad:** Baja (usuario diseñado para exhibir este bug)

## Evidencia
_Adjuntar captura de pantalla del catálogo con las imágenes duplicadas._

## Notas
Comportamiento intencional de SauceDemo; se documenta como ejercicio de reporte de defectos.
