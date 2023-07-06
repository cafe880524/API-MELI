from pydantic import BaseModel
from typing import Optional

class modelobd(BaseModel):
    _id: Optional[str]
    fec_alta: str
    user_name: str
    codigo_zip: str
    credit_card_num: str
    credit_card_ccv: str
    cuenta_numero: str
    direccion: str
    geo_latitud: str
    geo_longitud: str
    color_favorito: str
    foto_dni: str
    ip: str
    auto: str
    auto_modelo: str
    auto_tipo: str
    auto_color: str
    cantidad_compras_realizadas:int
    avatar: str
    fec_birthday: str
    id: str