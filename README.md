# backend-technical-test

## Índice

* [1. introduction](#1-consideraciones-generales)
* [2. Answers of bakend technical test](#2-respuestas)
* [3. Boilerplate](#4-boilerplate)
* [4. Conclusion](#4-Conslusion)


***

## 1. Introduction

Esta es una aplicación sencilla construida con Flask. Está diseñada para manejar la gestión de productos. La API permite a los usuarios realizar varias operaciones relacionadas con productos, tales como obtener una lista de productos y procesar datos.

En esta aplicación se usan los conceptos presentados por la empresa en el reto técnico. 

 **Instruction 1:**

    1. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

    2. Ejecuta la app con python app.py
    3. Verifica el resultado del GET en Postman o en tu local. 
    Ejemplos: http://127.0.0.1:5000/contacts/1
              http://127.0.0.1:5000/products

## 2. Answers of bakend technical test

1. **Question 1:** What verb should you choose to retrieve trade orders?
   - **Answer:** 1. GET
   - **Explanation:** GET es el verbo HTTP que se utiliza para recuparar datos del servidor. Realiza operaciones de solo lectura y no cambia el estado del recurso. El uso de GET minimiza la sobrecarga en comparación con otros verbos POSt, por lo que es la mejor opción para recuperar ordenes de negociación.

2. **Question 2:** What is the appropriate API path for clients to retrieve information about a contact?
   - **Answer:** 2. /contacts/{contact_id}
    - **Explanation:** La ruta /contacts/{contact_id} apunta directamente a un único contacto por su identificador único. Este enfoque es flexible para futuros cambios de software, lo que le permite administrar fácilmente diferentes tipos de contactos (clientes, clientes potenciales, etc.) Las otras opciones que me dan se centran en los clientes o pueden implicar una recuperación masiva, lo que no se alinea con el requisito de recuperar información para un solo contacto.

3. **Question 3:** What is the appropriate HTTP code for authentication failures?
   - **Answer:** 4. 401 if the user doesn't exist or if the password is incorrect.
   - **Explanation:**  El error 401 Unauthorized indica que se requiere autenticación y que ha fallado. Su uso tanto para usuarios inexistentes como para contraseñas incorrectas permite que el manejo de errores sea coherente y seguro. El error 404 podría hacer pensar a los clientes que no hay problemas de autenticación sino problemas con la página.

4. **Question 4:** Should you include a fake UUID in the example code?
   - **Answer:** 1. TRUE
   - **Explanation:** Incluir un UUID falso en el código de ejemplo ayuda a los usuarios a comprender el formato esperado de un UUID y cómo usarlo. Mejora la claridad de la documentación y proporciona un punto de referencia práctico, pero podría confundir a los usuarios y estos podrían llegar a pensar que identificador es real.

5. **Question 5:** What should the method handleErrors(response) do?
   - **Answer:** 2. Check for the presence of an error. If it exists, throw an exception with the error.
   - **Explanation:** Lanzar una excepción cuando se produce un error es una práctica estándar en el manejo de errores, ya que indica inmediatamente que algo salió mal y puede detectarse mediante una lógica de nivel superior.

6. **Question 6:** What is the best way to implement error handling across multiple classes?
   - **Answer:** 3. Create a driver-based error provider to handle errors in all classes.
   - **Explanation:** Creo que un proveedor de errores basado en controladores sería la mejor opción. Este promoverá la coherencia y será útil para el mantenimiento de las clases.

7. **Question 7:** How should you name the method that handles looping through eCommerce products?
   - **Answer:** 2. loopProductsAndParse()
   - **Explanation:** Este nombre es claro y al mismo tiempo evita usar demasiado texto. Las otras opciones son muy largas o son menos claras.

8. **Question 8:** What strategy should you use to store and access database credentials?
   - **Answer:** 4. Put them in a .env file, load the data into a configuration system, and then request the credentials from a database service provider.
   - **Explanation:** Usar un archivo .env para guardar la información confidencial tipo usuarios y contraseñas. Esta es un apráctica recomendada por diferentes Frameworks y Librerías y por OWASP para mantener seguros los datos.

## 3. Boilerplate

/backend-technical-test
│
 ├──src
        ├──aap.py
        ├──error_handler.py
        ├──.env
        ├── README.md
        ├──requirements.txt
        ├──.gitignore
      
## 4. Conclusion

Esta aplicación me permite mostrar algunos de mis conocimientos y pone en práctica los conceptos solicitados en la prueba técnica.

Me encantaría tener la oportunidad de hablar sobre cómo puedo aportar valor a su equipo. ¡Gracias por considerar mi candidatura!
