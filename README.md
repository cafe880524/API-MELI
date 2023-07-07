## API PARA LA CONSULTA DE CLIENTES MELI DESDE UN PROVEEDOR EXTERNO


Instrucciones de ejecución 

La API de Consulta de clientes, está construida bajo una arquitectura REST, desarrollada  Python3, sobre el framework web FASTAPI y desplegada en un servidor WEB uvicornm, con una base de datos NoSQL MongoDB. La solución se construyó en un ambiente Linux - Ubuntu 22.04 el cual se está ejecutando en una instancia EC2 de AWS

#Requisitos

•	Instalar la versión reciente de MongoDB para ubuntu, seguir los pasos de la documentación oficial 
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition

•	Instalar Python3, en mi caso utilice la versión ya instalada en el Ubuntu Python 3.10.6
$ sudo apt-get update
$ sudo apt-get install python3.10

•	Instalar el módulo pip3
$ sudo apt-get update
$ sudo apt-get install python3.6

•	Instalamos la librería Pymongo, la cual permite interactuar con MongoDB desde Python
https://pymongo.readthedocs.io/en/stable/installation.html

$  pip install pymongo
•	Instalamos pydantic, el cual es una biblioteca de validación de datos para Python
https://docs.pydantic.dev/latest/install/

$ pip install pydantic
•	Instalamos FastAPI, este framework permitirá crear API con Python 3.7+
https://fastapi.tiangolo.com/#typer-the-fastapi-of-clis

$ pip install fastapi
•	Instalamos uvicorn , el cual permite desplegar nuestra API en un servidor web
https://www.uvicorn.org/#quickstart

$ sudo pip install uvicorn

#Ejecución de la API

1.	Para la  ejecución de la API se debe contar con un sistema Ubuntu, para esta solución se utilizó la versión de Ubuntu 22.04 desplegado en una EC2 mediante Cloudformation
Puedes descargar el cloudformation utilizado: 
https://github.com/cafe880524/API-MELI/tree/main/anexos
2.	Instalar los requerimientos mencionados 
3.	Descargar el script de la API desde el repositorio API-MELI
git clone https://github.com/cafe880524/API-MELI.git
4.	Correr el archivo execute.sh para desplegar la API, este archivo contiene las siguientes instrucciones para:

sh execute.sh
o	Subir la base de datos mongodb por si esta se encuntra abajo
sudo systemctl start mongod
o	Capturar la ip del servidor en un parámetro IP, el cual se entrega como parámetro para desplegar el servidor uvircorn
IP=$(ip addr show |grep -w inet |grep -v 127.0.0.1|awk '{ print $2}'| cut -d "/" -f 1)
o	Subir el servidor uvicorn pasando como parámetro de host la ip del servidor
uvicorn main:app --reload --host $ip

#Consulta de Clientes

Posterior a que el servidor uvicorn se haya desplegado correctamente, ya podemos hacer uso de nuestra API, para consultar todos los clientes almacenados en la base de datos, o consultar cliente por cliente, pasando como parámetro el “id”. El  acceso al servicio se puede hacer de dos formas una haciendo una petición directa a la URL expuesta u utilizando la interfaz gráfica de usuario
Consulta directa a la URL expuesta del Servicio 
•	Para hacer la consultar de todos los usuarios, se debe abrir en el navegador web la siguiente URL (ipservidor -> es la ip en la cual se desplego la api)
http://ipservidor:8000/users

•	Para hacer la consultar de un usuario especifico por id, se debe abrir en el navegador web la siguiente URL (ipservidor -> es la ip en la cual se desplego la api), y remplazando un numero de id, en el parámetro id de la URL
http://ipservidor:8000/user/id

Consulta Mediante Interfaz Grafica  
Para acceder a la interfaz gráfica se debe abrir el navegador e ingresar a la siguiente la URL http://ipservidor:8000/docs

•	Para hacer la consultar de todos los usuarios, se debe seleccionar la opción Select All User , luego dar clic sobre la opción Try it out y por último en Execute

•	Para hacer la consultar de usuarios uno a uno por id, se debe seleccionar la opción Select One User , en el campo id, diligenciar el id del usuario, luego dar clic sobre la opción Try it out y por último en Execut
