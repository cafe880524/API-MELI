from fastapi import APIRouter ##Defien rutas dentrl del archivo
from config.db import conn
from esquemas.esquema import userEntity, usersEntity
from modulos.modelobd import  modelobd
from urllib.request import urlopen
##from passlib.hash import sha256_crypt
import json
import urllib.parse
from bson import ObjectId

rutaurl=APIRouter()

def select():
    result=conn.local.clientes.find()
    for result in result:
        return (result) 
    
def insert(resultado):
    if resultado == None:
        with urlopen("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios") as reponse:
            body =reponse.read()
        todo_item = json.loads(body)
        conn.local.clientes.insert_many(todo_item)
        print("Se Insertaron Datos")
    else:
        print("ya hay Datos Insertados")

# def deletedoc():
#     x=conn.local.clientes.delete_many({})
#     print(x.deleted_count, "Información de clientes Borrad")

# deletedoc()
resultado=select()
insert(resultado)


@rutaurl.get("/users/", tags=["Consulta Todos Los  Usuarios"])
def select_all_user():
    return usersEntity(conn.local.clientes.find())

@rutaurl.get("/user/{id}", tags=["Consulta de Usuarios por ID"])
def select_one_user(id: str):
    return userEntity(conn.local.clientes.find_one({"id":id}))
    







    

# @user.get("/user")
# def select_all_users(collecion):
#     result=collecion.find()
#     return result
    # for result in result:
    #     return result
    ##return (client.clientes_MELI.clientes.find())

# @user.get("/user/{id}")
# def select_one_user():
#     return "Hola Paula, que tal tu día"

