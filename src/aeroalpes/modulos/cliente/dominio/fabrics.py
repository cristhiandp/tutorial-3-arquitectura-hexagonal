from dataclasses import dataclass
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.entidades import Entidad
from .entidades import Cliente
from aeroalpes.seedwork.dominio.repositorios import Mapeador

@dataclass
class ClienteFactory(Fabrica):
    def crear_objeto(obj: any, mapeador: Mapeador) -> any:
        if(isinstance(obj, Entidad)):
            return mapeador.entidad_a_dto(obj)

        return mapeador.dto_a_entidad(obj)
        
    