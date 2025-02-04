from src.aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

class ExcepcionFabrica(ExcepcionDominio):
    def __init__(self, mensaje):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)