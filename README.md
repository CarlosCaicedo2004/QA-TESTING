# QA Portfolio CARLOS MAURICIO CAICEDO DIAGO

Portafolio de QA Testing enfocado en demostrar habilidades prácticas para un rol de **QA Tester Junior**, cubriendo pruebas manuales, automatización y testing de APIs.

## 📋 Contenido

### 1. Manual Testing (`/manual-testing`)
Pruebas manuales sobre [SauceDemo](https://www.saucedemo.com), una app de e-commerce de práctica.
- **[test-plan.md](./manual-testing/test-plan.md)**: alcance, estrategia y ambiente de pruebas
- **[test-cases.csv](./manual-testing/test-cases.csv)**: 25 casos de prueba cubriendo login, catálogo, carrito y checkout
- **[bug-reports/](./manual-testing/bug-reports/)**: defectos encontrados y documentados, con pasos de reproducción, severidad/prioridad y evidencia

**Hallazgo destacado:** al usar el usuario `problem_user`, se detectó que las imágenes de los productos no corresponden a cada artículo (ver [BUG-001](./manual-testing/bug-reports/BUG-001-imagenes-incorrectas-problem-user.md)).

### 2. Automation (`/automation-selenium-python`) — *próximamente*
Scripts de automatización con Selenium/Cypress cubriendo los flujos críticos (login, checkout).

### 3. API Testing (`/api-testing-postman`) — *próximamente*
Colección de Postman probando endpoints de una API pública de e-commerce.

## 🛠️ Herramientas usadas
- Documentación: Markdown, CSV
- App bajo prueba: [SauceDemo](https://www.saucedemo.com)
- Próximamente: Selenium, Cypress, Postman, Git

## 🎯 Sobre este portafolio
Este repositorio demuestra, de forma práctica, el ciclo completo de QA manual: desde la planificación (test plan) hasta el diseño de casos de prueba y el reporte estructurado de defectos, como base para avanzar hacia automatización y testing de APIs.
