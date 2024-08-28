# Análisis de Opiniones Académicas - README

## Descripción

Este proyecto se enfoca en el desarrollo y uso de una aplicación web o móvil gratuita y accesible para la recolección de opiniones académicas. La aplicación permite a los usuarios proporcionar retroalimentación sobre diversos aspectos académicos y pedagógicos. Los datos recolectados se procesan y analizan a través de un servidor, que ofrece medidas básicas de estadística descriptiva para apoyar la creación de reportes detallados y análisis de tendencias.

## Palabras Clave

- Análisis de sentimientos
- Comunidades universitarias
- Problemas académicos
- Retroalimentación pedagógica
- Procesamiento de lenguaje natural (NLP)
- Algoritmos de machine learning
- Estadística descriptiva
- Informe académico
- Retroalimentación educativa
- Opiniones académicas
- Evaluación docente
- Evaluación crítica
- Tendencias del curso

## Instrucciones para el Uso del API

### Base URL

Reemplaza `{{base_url}}` con la URL base de tu servidor API en todas las solicitudes.

### Endpoints Disponibles

#### 1. Registro de Usuario

- **URL:** `{{base_url}}/api/user/register`
- **Método:** POST
- **Cuerpo de la Solicitud:**
  ```json
  {
    "name": "Sebastian Gamez",
    "email": "juan@gmail.com",
    "password": "otrapass",
    "role": "monitor"
  }
  ```

#### 2. Inicio de Sesión de Usuario

- **URL:** `{{base_url}}/api/user/login`
- **Método:** POST
- **Cuerpo de la Solicitud:**
  ```json
  {
    "email": "juan@gmail.com",
    "password": "otrapass"
  }
  ```

#### 3. Crear Pregunta

- **URL:** `{{base_url}}/api/question/create`
- **Método:** POST
- **Cuerpo de la Solicitud:**
  ```json
  {
    "question": "¿Quién es el rector legítimo?"
  }
  ```

#### 4. Obtener Pregunta por ID

- **URL:** `{{base_url}}/api/question/{id_question}`
- **Método:** GET
- **Parámetros de URL:**
  - `id_question`: El ID de la pregunta a obtener.

#### 5. Obtener Todas las Preguntas

- **URL:** `{{base_url}}/api/question/all`
- **Método:** GET

#### 6. Crear Análisis

- **URL:** `{{base_url}}/api/analysis/create`
- **Método:** POST
- **Cuerpo de la Solicitud:**
  ```json
  {
    "answer": "Peña fue elegido bajo el proceso actual; sin embargo, este no contempla la opinión de los estudiantes. La legitimidad es subjetiva",
    "question_id": 1,
    "user_id": 1
  }
  ```

#### 7. Obtener Análisis por Usuario

- **URL:** `{{base_url}}/api/analysis/user/{id_user}`
- **Método:** GET
- **Parámetros de URL:**
  - `id_user`: El ID del usuario cuyos análisis se desean obtener.

#### 8. Obtener Análisis por Pregunta

- **URL:** `{{base_url}}/api/analysis/question/{id_question}`
- **Método:** GET
- **Parámetros de URL:**
  - `id_question`: El ID de la pregunta cuyos análisis se desean obtener.

#### 9. Estadísticas de Análisis por Usuario

- **URL:** `{{base_url}}/api/analysis/user/statistics/{id_user}`
- **Método:** GET
- **Parámetros de URL:**
  - `id_user`: El ID del usuario para el cual se desean obtener las estadísticas.

#### 10. Estadísticas de Análisis por Pregunta

- **URL:** `{{base_url}}/api/analysis/question/statistics/{id_question}`
- **Método:** GET
- **Parámetros de URL:**
  - `id_question`: El ID de la pregunta para la cual se desean obtener las estadísticas.

## Ejemplos de Solicitudes

### Ejemplo de Solicitud para Registro de Usuario

```sh
curl -X POST {{base_url}}/api/user/register \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Sebastian Gamez",
           "email": "juan@gmail.com",
           "password": "otrapass",
           "role": "monitor"
         }'
```

### Ejemplo de Solicitud para Inicio de Sesión de Usuario

```sh
curl -X POST {{base_url}}/api/user/login \
     -H "Content-Type: application/json" \
     -d '{
           "email": "juan@gmail.com",
           "password": "otrapass"
         }'
```

### Ejemplo de Solicitud para Obtener Todas las Preguntas

```sh
curl -X GET {{base_url}}/api/question/all
```

### Ejemplo de Solicitud para Crear un Análisis

```sh
curl -X POST {{base_url}}/api/analysis/create \
     -H "Content-Type: application/json" \
     -d '{
           "answer": "Peña fue elegido bajo el proceso actual; sin embargo, este no contempla la opinión de los estudiantes. La legitimidad es subjetiva",
           "question_id": 1,
           "user_id": 1
         }'
```

## Notas Adicionales

- Asegúrate de manejar los errores y las respuestas de la API adecuadamente.
- Los parámetros de URL entre llaves (`{}`) deben ser reemplazados con valores reales.
- Las solicitudes POST deben incluir los encabezados correctos y el cuerpo en formato JSON.

Para más detalles, revisa la documentación específica de cada endpoint y sigue las mejores prácticas en el desarrollo de API.

## Enlace del repositorio: 
https://github.com/SebastianGamez/sentiment__analysis/
