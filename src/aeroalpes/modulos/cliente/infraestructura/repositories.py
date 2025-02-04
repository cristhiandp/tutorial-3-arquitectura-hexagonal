from aeroalpes.modulos.cliente.dominio.repositories import ClientRepository
from aeroalpes.modulos.cliente.dominio.entidades import ClienteEmpresa

class ClientRepositorySQLLite(ClientRepository):
    def agregar(self, entity: ClienteEmpresa):
        ...

class ClientRepositoryPostgres(ClientRepository):
    def agregar(self, entity: ClienteEmpresa):
        ...
