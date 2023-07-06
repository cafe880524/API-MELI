# from pymongo import MongoClient
# from  fastapi import FastAPI


# app = FastAPI()

# mongo_uri = "mongodb://localhost"
# client = MongoClient(mongo_uri)

# bd=client["Clientes_MELI"]
# collecion=bd["clientes"]


# @app.get("/user")
# def select_all_users(collecion):
#     result=collecion.find({"id":"10"})
#     return result

# @app.get("/user/{id}")
# def select_one_user():
#     return "Hola Paula, que tal tu día"