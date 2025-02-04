from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from aeroalpes.modulos.cliente.dominio.repositories import ClientRepository
from .repositories import ClientRepositorySQLLite
from .exceptions import ExcepcionFabrica

class RepositoryFactory(Fabrica):
    def crear_objeto(self, obj: any) -> Repositorio:
        if obj == ClientRepository.__class__:
            return ClientRepositorySQLLite()
        return ExcepcionFabrica()

    