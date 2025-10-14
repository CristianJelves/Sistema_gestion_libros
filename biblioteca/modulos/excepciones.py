# Excepción para cuando un libro no está disponible
class LibroNoDisponible(Exception):
    def __init__(self, mensaje="El libro no está disponible para préstamo."):
        super().__init__(mensaje)


# Excepción para cuando un usuario no está registrado
class UsuarioNoRegistrado(Exception):
    def __init__(self, mensaje="El usuario no está registrado en el sistema."):
        super().__init__(mensaje)


# Excepción para cuando se intenta duplicar un préstamo
class PrestamoDuplicado(Exception):
    def __init__(self, mensaje="Este préstamo ya fue registrado."):
        super().__init__(mensaje)