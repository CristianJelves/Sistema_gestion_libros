class Prestamo:
    # Representa el préstamo de un libro a un usuario

    def __init__(self, libro, usuario):
        # Inicializa el préstamo con un libro y un usuario
        self._libro = libro        # Objeto de tipo Libro
        self._usuario = usuario    # Objeto de tipo Usuario

    def realizar_prestamo(self):
        # Intenta prestar el libro si está disponible
        if self._libro.esta_disponible():
            self._libro.prestar()  # Marca el libro como prestado
            print("Préstamo realizado con éxito.")
            print(f"Libro: {self._libro._titulo} → Usuario: {self._usuario._nombre}")
        else:
            print("El libro ya está prestado. No se puede realizar el préstamo.")

    def mostrar_info(self):
        # Muestra los detalles del préstamo
        print(f"Libro: {self._libro._titulo} prestado a {self._usuario._nombre}")