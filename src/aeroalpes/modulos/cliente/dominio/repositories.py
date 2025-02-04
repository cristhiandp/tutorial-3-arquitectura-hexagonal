from abc import ABC, abstractmethod
from uuid import UUID
from aeroalpes.seedwork.dominio.repositorios import Repositorio

class ClientRepository(ABC, Repositorio):
    ...
