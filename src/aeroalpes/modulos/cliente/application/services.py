from aeroalpes.seedwork.aplicacion.servicios import Servicio
from aeroalpes.modulos.cliente.infraestructura.fabrics import RepositoryFactory
from aeroalpes.modulos.cliente.dominio.fabrics import ClienteFactory
from aeroalpes.modulos.cliente.dominio.entidades import ClienteEmpresa
from .dto import ClienteDTO
from aeroalpes.modulos.cliente.infraestructura.repositories import ClientRepository

class ClientService(Servicio):

    def __init__(self):
        self._fabrica_repositorio: RepositoryFactory = RepositoryFactory()
        self._fabrica_clientes: ClienteFactory = ClienteFactory()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes
    
    def crear_cliente(self, cliente_dto: ClienteDTO) -> ClienteDTO:
        client: ClienteEmpresa = self.fabrica_clientes.crear_objeto(cliente_dto)
        repositorio = self.fabrica_repositorio.crear_objeto(ClientRepository.__class__)
        repositorio.agregar(client)

        return self.fabrica_clientes.crear_objeto(client)
    
