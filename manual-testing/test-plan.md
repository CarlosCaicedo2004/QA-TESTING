# Test Plan — SauceDemo E-commerce Web App

## 1. Introducción
Este documento describe el plan de pruebas funcionales para la aplicación web [SauceDemo](https://www.saucedemo.com), un sitio de e-commerce de práctica utilizado para demostrar habilidades de QA manual.

## 2. Objetivo
Validar que los flujos principales (autenticación, catálogo de productos, carrito y checkout) funcionen según el comportamiento esperado, e identificar defectos que afecten la experiencia del usuario.

## 3. Alcance

### Dentro del alcance
- Login / Logout (usuarios `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`)
- Listado y ordenamiento de productos (por nombre y precio)
- Agregar/quitar productos del carrito
- Flujo completo de checkout (datos del comprador, resumen de orden, confirmación)
- Navegación general (menú lateral, botones de regreso)

### Fuera del alcance
- Pruebas de rendimiento y carga
- Pruebas de seguridad
- Compatibilidad cross-browser exhaustiva (solo Chrome de escritorio)
- Pruebas de accesibilidad (WCAG)

## 4. Estrategia de pruebas
- **Tipos:** funcionales, de regresión y exploratorias
- **Técnicas de diseño:** particiones de equivalencia, valores límite, tablas de decisión
- **Enfoque:** pruebas manuales basadas en casos documentados, complementadas con pruebas exploratorias para detectar comportamientos inesperados

## 5. Criterios de entrada
- La aplicación está disponible en https://www.saucedemo.com
- Los casos de prueba fueron diseñados y revisados

## 6. Criterios de salida
- 100% de los casos planificados ejecutados
- Defectos críticos y altos documentados y reportados
- Sin bloqueadores sin registrar

## 7. Ambiente de pruebas
- **Navegador:** Google Chrome (última versión estable)
- **Sistema operativo:** Windows
- **URL:** https://www.saucedemo.com
- **Usuarios de prueba:** públicos de SauceDemo (standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user), contraseña `secret_sauce`

## 8. Entregables
- Este test plan
- Casos de prueba (`test-cases.csv`)
- Reportes de bugs (`bug-reports/`)

## 9. Riesgos
| Riesgo | Impacto | Mitigación |
|---|---|---|
| El sitio es de práctica y puede cambiar sin aviso | Medio | Validar los casos antes de cada ejecución |
| Usuarios especiales (problem_user, etc.) tienen bugs intencionales | Bajo | Documentarlos como hallazgos esperados |

## 10. Roles
- **Diseño y ejecución de pruebas:** [Tu nombre]
- **Reporte de defectos:** [Tu nombre]
