from dataclasses import dataclass
from aeroalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ClientDTO(DTO):
    name: str
    last_name: str
    email: str
    phone: str