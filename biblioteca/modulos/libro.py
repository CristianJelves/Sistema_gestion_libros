class Libro:
    # Representa un libro en la biblioteca

    def __init__(self, titulo, autor, genero):
        # Inicializa el libro con título, autor, género y disponibilidad
        self._titulo = titulo            # Título del libro (protegido)
        self._autor = autor              # Autor del libro (protegido)
        self._genero = genero            # Género del libro (protegido)
        self._disponible = True          # True si el libro está disponible, False si está prestado

    def mostrar_info(self):
        # Muestra en consola los detalles del libro
        estado = "Disponible" if self._disponible else "Prestado"
        print(f"Título: {self._titulo} | Autor: {self._autor} | Género: {self._genero} | Estado: {estado}")

    def esta_disponible(self):
        # Devuelve True si el libro está disponible, False si está prestado
        return self._disponible

    def prestar(self):
        # Marca el libro como prestado
        self._disponible = False

    def devolver(self):
        # Marca el libro como disponible
        self._disponible = True
