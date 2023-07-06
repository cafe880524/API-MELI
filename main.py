
from  fastapi import FastAPI
from rutas.rutasURL import rutaurl

app = FastAPI(
    title="API Rest para consultar clientes" ,
    description = "Esta API permite a los equipos de MELI consultar información Clientes extraidos de un proveedor externo "
    , version="1.0"
)


app.include_router(rutaurl)





