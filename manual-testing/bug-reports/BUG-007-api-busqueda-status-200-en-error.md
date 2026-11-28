# BUG-007: La API de búsqueda devuelve status HTTP 200 cuando la petición es inválida

## Resumen
Al llamar a `POST /api/searchProduct` sin el parámetro obligatorio `search_product`, la API responde con status HTTP 200, mientras que el body indica `responseCode: 400`. El encabezado HTTP y el body se contradicen.

## Entorno
- **URL:** https://automationexercise.com/api/searchProduct
- **Herramienta:** Postman
- **Método:** POST (body form-data vacío)

## Pasos para reproducir
1. En Postman, crear una petición POST a https://automationexercise.com/api/searchProduct
2. No enviar ningún parámetro en el body
3. Click en Send
4. Comparar el Status HTTP con el contenido del body

## Resultado actual
- Status HTTP: 200 OK
- Body: {"responseCode": 400, "message": "Bad request, search_product parameter is missing in POST request."}

## Resultado esperado
Una petición inválida debería responder con status HTTP 400 en el encabezado, coherente con el responseCode del body.

## Impacto
Cualquier cliente (una app, un script de pruebas) que solo revise el status HTTP interpretará el error como una búsqueda exitosa y no manejará el fallo.

## Severidad / Prioridad
- **Severidad:** Media
- **Prioridad:** Media

## Evidencia
[Captura de Postman con el status 200 y el body con responseCode 400]

## Notas
Detectado en testing de API con Postman. También se observa en `POST /api/verifyLogin` con credenciales inválidas (status 200, responseCode 404). El patrón se repite en más de un endpoint.
