# backend-technical-test

## Índice

* [1. Introducción](#1-introducción)
* [2. Respuestas del reto técnico](#2-respuestas-del-reto-técnico)
* [3. Boilerplate](#3-boilerplate)
* [4. Conclusión](#4-conclusión)

***

## 1. Introducción

Esta es una aplicación sencilla construida con Flask. Está diseñada para manejar la gestión de productos. La API permite a los usuarios realizar varias operaciones relacionadas con productos, tales como obtener una lista de productos.

En esta aplicación se usan los conceptos presentados en el reto técnico. Hay que considerar que en esta aplicación se hace una simulación de los datos de los clientes. En un entorno de trabajo se debe realizar la conexión a la base de datos. También es importante mencionar que se crea un archivo con variables de entorno llamado .env que no es usado y que se presenta como ejemplo en relación con la pregunta número 8.

**Instrucciones:**

Para usar esta app sigue estas instrucciones.

1. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

2. Ejecuta la app con:
    ```bash
    python app.py
    ```

3. Verifica el resultado del GET en Postman (preferiblemente) o en tu local. 
   Ejemplos:
   - `http://127.0.0.1:5000/contacts/1`
   - `http://127.0.0.1:5000/products`

## 2. Respuestas del reto técnico

1. **Pregunta 1:** ¿Qué verbo deberías elegir para recuperar órdenes de comercio?
   - **Respuesta:** 1. GET
   - **Explicación:** GET es el verbo HTTP que se utiliza para recuperar datos del servidor. Realiza operaciones de solo lectura y no cambia el estado del recurso. El uso de GET minimiza la sobrecarga en comparación con otros verbos POST, por lo que es la mejor opción para recuperar órdenes de negociación.

2. **Pregunta 2:** ¿Cuál es la ruta API adecuada para que los clientes recuperen información sobre un contacto?
   - **Respuesta:** 2. /contacts/{contact_id}
   - **Explicación:** La ruta /contacts/{contact_id} apunta directamente a un único contacto por su identificador único. Este enfoque es flexible para futuros cambios de software, lo que le permite administrar fácilmente diferentes tipos de contactos (clientes, clientes potenciales, etc.). Las otras opciones que me dan se centran en los clientes o pueden implicar una recuperación masiva, lo que no se alinea con el requisito de recuperar información para un solo contacto.

3. **Pregunta 3:** ¿Cuál es el código HTTP apropiado para fallos de autenticación?
   - **Respuesta:** 4. 401 si el usuario no existe o si la contraseña es incorrecta.
   - **Explicación:** El error 401 Unauthorized indica que se requiere autenticación y que ha fallado. Su uso tanto para usuarios inexistentes como para contraseñas incorrectas permite que el manejo de errores sea coherente y seguro. El error 404 podría hacer pensar a los clientes que no hay problemas de autenticación sino problemas con la página.

4. **Pregunta 4:** ¿Deberías incluir un UUID falso en el código de ejemplo?
   - **Respuesta:** 1. TRUE
   - **Explicación:** Incluir un UUID falso en el código de ejemplo ayuda a los usuarios a comprender el formato esperado de un UUID y cómo usarlo. Mejora la claridad de la documentación y proporciona un punto de referencia práctico, pero podría confundir a los usuarios y estos podrían llegar a pensar que el identificador es real.

5. **Pregunta 5:** ¿Qué debería hacer el método handleErrors(response)?
   - **Respuesta:** 2. Comprobar la presencia de un error. Si existe, lanzar una excepción con el error.
   - **Explicación:** Lanzar una excepción cuando se produce un error es una práctica estándar en el manejo de errores, ya que indica inmediatamente que algo salió mal y puede detectarse mediante una lógica de nivel superior.

6. **Pregunta 6:** ¿Cuál es la mejor manera de implementar el manejo de errores en múltiples clases?
   - **Respuesta:** 3. Crear un proveedor de errores basado en controladores para manejar errores en todas las clases.
   - **Explicación:** Creo que un proveedor de errores basado en controladores sería la mejor opción. Este promoverá la coherencia y será útil para el mantenimiento de las clases.

7. **Pregunta 7:** ¿Cómo deberías nombrar el método que maneja el bucle a través de los productos de comercio electrónico?
   - **Respuesta:** 2. loopProductsAndParse()
   - **Explicación:** Este nombre es claro y al mismo tiempo evita usar demasiado texto. Las otras opciones son muy largas o son menos claras.

8. **Pregunta 8:** ¿Qué estrategia deberías usar para almacenar y acceder a las credenciales de la base de datos?
   - **Respuesta:** 4. Colocarlas en un archivo .env, cargar los datos en un sistema de configuración y luego solicitar las credenciales a un proveedor de servicios de base de datos.
   - **Explicación:** Usar un archivo .env para guardar la información confidencial, tipo usuarios y contraseñas. Esta es una práctica recomendada por diferentes Frameworks y Librerías y por OWASP para mantener seguros los datos.

## 3. Boilerplate

A continuación se muestra la estructura del proyecto:

/backend-technical-test
│
  ├──src
    │   ├──aap.py
    │   ├──error_handler.py
    │   ├──.env
    │   ├── README.md
    │   ├──requirements.txt
    │   ├──.gitignore

## 4. Conclusión

Esta aplicación me permite mostrar algunos de mis conocimientos y pone en práctica los conceptos solicitados en la prueba técnica.

Me encantaría tener la oportunidad de hablar sobre cómo puedo aportar valor a su equipo. ¡Gracias por considerar mi candidatura!
