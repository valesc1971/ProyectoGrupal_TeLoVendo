# Proyecto Campcake - Modulo 6 ABPro6

Este proyecto consiste es una pagina web para un negocio independiente que permite presentar la empresa y recibir pedidos de clientes. 
En este caso particular, se trata de una panaderia-pasteleria de nombre CampCake.
Este proyecto permite automatizar la administración y entrega de los productos de la empresa a través de internet a sus clientes. 
Esto contempla sus productos de panadería, pastelería y minimarket. 

## Tabla de Contenidos

* [Tecnologias Usadas](#Tecnologias)
* [Instalacion](#Instalacion)
* [Consideraciones](#Consideraciones)
* [Visualizacion del sitio web](#Visualizacion)

<a name="Tecnologias"></a>
## Tecnologias

Este proyecto fue creado usando:
* HTML
* CSS
* Boostrap   (https://getbootstrap.com/)
* JavaScript (https://datatables.net/)
* JQuery    (https://jquery.com/)
* DataTable plugin
* Python 3.10.4
* Django 4.0.4

<a name="Instalacion"></a>
## Instalacion
Para descargar este proyecto, se debe clonar desde este repositorio remoto a un repositorio local.

$git clone https://github.com/valesc1971/ProyectoGrupal_TeLoVendo.git

Luego se debe utilizar el editor de código Visual Studio Code. Se requiere tener instalado el lenguaje Python en el equipo.
Posteriomente estando en la terminal del editor, se debe abrir y activar un entorno virtual con la instrucción virtualenv env/Scripts/activate. 
Se requiere también tener instalado el framework Django. De no ser así se debe instalar en la terminal con la instrucción pip install Django. 
Finalmente, para ejecutar el programa se debe levantar el servidor en Python con la instrucción py manage.py runserver. 

<a name="Consideraciones"></a>
## Consideraciones

Este proyecto es una continuacion del proyecto ubicado en XXXXXXX.Para la informacion inicial de esteproyecto, favor revisar el archivo readme de ese repositorio (Consideraciones)

Adicionalmente, se usa el framework Django y lenguiaje Python para administrar el sistema. 

El sistema cuenta con un menú, en el cual se muestran distintas opciones para ser utilizados por los usuarios, tales como Productos, Pedidos, 
Estadísticas, Ingreso Clientes, Login y salir. 

Restricciones:
El menú Listado de clientes solo puede ser utilizado por los usuarios registrados. Cuando un usuario se registra y se loguea, el sistema le da un mensaje personalizado de de bienvenida. 
Si el usuario no está registrado no puede acceder a la página de bienvenida. En la opción usuarios se muestra información estadistica de clientes; 
en Ingresar Clientes aparece un formulario para que los clientes que quieran comprar en línea puedan hacerlo, ingresando sus datos. En Login los usuarios registrados
pueden acceder al sistema, el cual les da un mensaje de bienvenida y en Salir el usuario sale del sistema con un mensaje de despedida."

Permisos administrativos:
Se crearon 3 grupos de usuarios: GrupoClientes, GrupoProductos y GrupoPedidos. Cada uno de estos grupos tiene asignado 1 usuarios con permisos CRUD para su respectivo grupo. Por ejemplo, si el suaurio esta asignado al GrupoPedidos, solo tiene visibilidad de la informacion de Pedidos.


<a name="Visualizacion"></a>
## Visualizacion del sitio web
![image](https://user-images.githubusercontent.com/99301347/153718537-06c6ce1f-00cf-45ed-9460-52f8c606e2f3.png)
![image](https://user-images.githubusercontent.com/99301347/153718564-b28cc154-52f0-4cd9-aa8a-ea23b763074d.png)
![image](https://user-images.githubusercontent.com/99301347/153718585-e1aab1fc-2ca2-4c3e-9489-e2dbf1125cdc.png)
![image](https://user-images.githubusercontent.com/99301347/153718607-d85fca0b-2aec-4ea0-b71e-9b675088b7b8.png)
![image](https://user-images.githubusercontent.com/99301347/166082096-b8c4ae71-3859-4c96-8e21-11b8bab6f3fa.png)
![image](https://user-images.githubusercontent.com/99301347/166082101-ea6bf90c-bec1-48d7-8ca0-06afab75a108.png)
![image](https://user-images.githubusercontent.com/99301347/166082109-e3479678-21bf-4456-9a71-8cc9634ba6b7.png)
![image](https://user-images.githubusercontent.com/99301347/166082112-7fa56657-3b46-4b98-9768-31637382d692.png)





Este grupo de trabajo está conformado por:
Valeria Sanchez, Fernando Quezada, Carlos Galleguillos y Alejandro Lanas.

Ningún derecho reservado, disponible para su copia, modificación y/o distribución en pos del aprendizaje.
