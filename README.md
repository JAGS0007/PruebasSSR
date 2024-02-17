Bienvenidos a mi proyecto de automatización del portal web "Despegar", estos son las bases en las que esta realizado el proyecto:
- Lenguaje: Python
- Tipo de Proyecto: PyCharm
- Framework de ejecución: Junit
- Framework de pruebas: Selenium
- Driver: Chrome
- Arquetipo: POM

Iniciamos con la sección de Enviroment, en la cual contiene el menu principal para generar toda la automatización (La cabeza)

Continuamos con Funciones basicas en la sección de Basic, tales como la apertura y levantamiento del navegador.
Con un dinamismo de actualización del driver, esto con el fin de garantizar que sin importar la version del driver, se pueda seguir ejecutando.
Luego contamos con las funciones basicas, tales como, tiempo, credenciales, en caso de necesitarlas, lectura de localizadores dinamica, entre otras.

Para el proceso, de escaneo de archivo externo .XLSX, donde se almacenara todos los posibles escenarios de ejecución,
con sus respectivos resultados, de esta misma manera se genera una creación de un archivo tipo .xlsx donde almacenara la información del resultado restante de la ejecución de la prueba.
En paralelo, se ejecutara una función para identificar cada campo, donde se pueda tomar toda la información y sacar un resultado satisfactorio.

Por consiguiente el archivo consultar y recepción son para cumplir con las demandas especificadas por el usuario.