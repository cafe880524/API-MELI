
def userEntity(item)-> dict:
    return{
        "_id" :str(item["_id"]),
        "fec_alta":item["fec_alta"],
        "user_name":item["user_name"],
        "ip":item["ip"],
        "auto":item["auto"],
        "auto_modelo":item["auto_modelo"],
        "auto_tipo":item["auto_tipo"],
        "auto_color":item["auto_color"],
        "cantidad_compras_realizadas":item["cantidad_compras_realizadas"],
        "avatar":item["avatar"],
        "id":item["id"]

    }

# def userEntity(item)-> dict:
#     return{
#         "_id" :str(item["_id"]),
#         "fec_alta":item["fec_alta"],
#         "user_name":item["user_name"],
#         "codigo_zip":item["codigo_zip"],
#         "credit_card_num":item["credit_card_num"],
#         "credit_card_ccv":item["credit_card_ccv"],
#         "cuenta_numero":item["cuenta_numero"],
#         "direccion":item["direccion"],
#         "geo_latitud":item["geo_latitud"],
#         "geo_longitud":item["geo_longitud"],
#         "color_favorito":item["color_favorito"],
#         "foto_dni":item["foto_dni"],
#         "ip":item["ip"],
#         "auto":item["auto"],
#         "auto_modelo":item["auto_modelo"],
#         "auto_tipo":item["auto_tipo"],
#         "auto_color":item["auto_color"],
#         "cantidad_compras_realizadas":item["cantidad_compras_realizadas"],
#         "avatar":item["avatar"],
#         "fec_birthday":item["fec_birthday"],
#         "id":item["id"]

#     }


def usersEntity(entity) -> list:
   return [userEntity(item) for item in entity]