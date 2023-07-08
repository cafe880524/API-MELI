
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


def usersEntity(entity) -> list:
   return [userEntity(item) for item in entity]
