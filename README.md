# FastAPI Backend

Este proyecto es una aplicación backend desarrollada con [FastAPI](https://fastapi.tiangolo.com/es/), un framework moderno y de alto rendimiento para construir APIs con Python.

## Características

- **Endpoints CRUD para usuarios**:
  - Crear un usuario con un ID único.
  - Leer información de un usuario por `user_id`.
  - Actualizar información de un usuario.
  - Eliminar un usuario por `user_id`.

## Instalación

1. **Clonar el repositorio**:

    ```bash
    git clone https://github.com/juanpa1999/FastAPI-backedn.git
    cd FastAPI-backedn
    ```

2. **Instalar las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Iniciar el servidor de desarrollo**:

    ```bash
    uvicorn main:app --reload
    ```

4. **Acceder a la documentación interactiva**:

    Abre tu navegador y ve a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para interactuar con la API utilizando la interfaz proporcionada por Swagger UI.

5. **Desplegar base de datos**:

    ```bash
    cd FastAPI-backedn/internal
    docker compose up -d
    ```

## Endpoints de la API

- **Crear usuario**

  - **Endpoint**: `POST /users`
  - **Descripción**: Crea un nuevo usuario con un `user_id` único.
  - **Cuerpo de la solicitud**:

    ```json
    {
      "name": "string",
      "age": "integer"
    }
    ```

- **Obtener todos los usuarios**

  - **Endpoint**: `GET /users`
  - **Descripción**: Retorna una lista de todos los usuarios.

- **Obtener usuario por ID**

  - **Endpoint**: `GET /users/{user_id}`
  - **Descripción**: Recupera los detalles de un usuario específico por su `user_id`.

- **Actualizar usuario**

  - **Endpoint**: `PUT /users/{user_id}`
  - **Descripción**: Actualiza el `name` y/o `age` del usuario especificado.
  - **Parámetros de consulta opcionales**: `?name=&age=`

- **Eliminar usuario**

  - **Endpoint**: `DELETE /users/{user_id}`
  - **Descripción**: Elimina un usuario por su `user_id`.

## Notas adicionales

Este proyecto utiliza la estructura de directorios recomendada para aplicaciones FastAPI, incluyendo carpetas como `models`, `routers`, `internal` y `dependencies` para una mejor organización del código.

Para más información sobre FastAPI y sus características, visita la [documentación oficial](https://fastapi.tiangolo.com/es/).

