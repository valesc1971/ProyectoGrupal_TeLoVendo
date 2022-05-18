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
* PostgreSQL

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

Este proyecto es una continuacion del proyecto ubicado en https://github.com/valesc1971/ABPro7.git .Para la informacion inicial de este proyecto, favor revisar el archivo readme de ese repositorio (Consideraciones)

Adicionalmente, se usa el framework Django y lenguaje Python para administrar el sistema. 

El sistema cuenta con un menú, en el cual se muestran distintas opciones para ser utilizados por los usuarios, tales como Productos, Pedidos, 
Estadísticas, Ingreso Clientes, Login y Salir. 

El registro de usuarios se puede hacer tanto desde la pagina principal como del admin de Django. sin embargo, la asignacion de permisos, grupos y tipos de usuarios se deben hacer desde el admin de Django por parte del superusuario.

Se realizo la migracion de base de datos desde SQLite a PostgreSQL

Se agrego una nueva clase de Proveedores para registrar los datos de proveedores de la empresa.

Se creo otra clase de Comentarios que tiene como objetivo que el cliente ingrese comentarios respecto a los productos de la empresa. Estos comentarios, se pueden crear, filtrar usando el email del usuario y se pueden editar o eliminar. 
Los comentarios se pueden ingresar con la opcion Comentarios ubicada en la barra de navegacion

![image](https://user-images.githubusercontent.com/99301347/167232744-03732295-7f5a-4456-bc68-cb685a2ac558.png)

Para  filtrar, editar o eliminar los comentarios, se debe usar la opcion Lista Comentarios en la barra de navegacion

![image](https://user-images.githubusercontent.com/99301347/167232732-6b6a4b2c-0490-4b4f-961d-c4650ecb4af0.png)


**Restricciones**:
El menú Listado de clientes solo puede ser utilizado por los usuarios registrados. Cuando un usuario se registra y se loguea, el sistema le da un mensaje personalizado de bienvenida. 
Si el usuario no está registrado no puede acceder a la página de bienvenida. 
En la opción usuarios se muestra información estadistica de clientes.
En Ingresar Clientes aparece un formulario para que los clientes que quieran comprar en línea puedan hacerlo, ingresando sus datos. 
En Login los usuarios registrados pueden acceder al sistema, el cual les da un mensaje de bienvenida.
En Salir el usuario sale del sistema con un mensaje de despedida.

**Permisos administrativos**:
Se crearon 3 grupos de usuarios: GrupoClientes, GrupoProductos y GrupoPedidos. 
Cada uno de estos grupos tiene asignado 1 usuario con permisos CRUD para su respectivo grupo. Por ejemplo, si el usuario esta asignado al GrupoPedidos, solo tiene visibilidad de la informacion de Pedidos.

**Relaciones entre Modelos de la Base de Datos**:
Se agregaron 2 modelos (Categoria y Subcategoria) para hacer relaciones 1 a muchos con el Modelo Proveedor, de tal forma que cuando se crea o registra un nuevo Proveedor, se debe seleccionar el tipo de Categoria y el de Subcategoria. Esto se puede visualizar en el admin de la aplicacion. El diagrama Entidad-Relacion de la base de datos, se encuentra en el archivo Diagrama Entidad Relacion - Grupal.pdf.

![image](https://user-images.githubusercontent.com/99301347/167749902-25846125-4850-4ff7-8b63-694942e5256b.png)
![image](https://user-images.githubusercontent.com/99301347/167749954-592a701a-814c-43d4-8a9e-b1e5c27721b2.png)



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
![image](https://user-images.githubusercontent.com/99301347/166083493-de5dc76c-efbc-40ae-8489-6588ee17685b.png)






Este grupo de trabajo está conformado por:
Valeria Sanchez, Fernando Quezada, Carlos Galleguillos y Alejandro Lanas.

Ningún derecho reservado, disponible para su copia, modificación y/o distribución en pos del aprendizaje.
