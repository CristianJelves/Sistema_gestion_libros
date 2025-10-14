class Usuario:
    # Clase para representar cualquier tipo de usuario
    def __init__(self, nombre, correo):
        # Inicializa el usuario con nombre y correo
        self._nombre = nombre        # Nombre del usuario (protegido)
        self._correo = correo        # Correo electrónico (protegido)

    def mostrar_info(self):
        # Muestra la información básica del usuario
        print(f"Nombre: {self._nombre} | Correo: {self._correo} | Rol: Usuario")


class Estudiante(Usuario):
    # Subclase que representa a un estudiante

    def __init__(self, nombre, correo, carrera):
        # Inicializa los atributos heredados y agrega carrera
        super().__init__(nombre, correo)  # Llama al constructor de Usuario
        self._carrera = carrera           # Carrera del estudiante

    def mostrar_info(self):
        # Muestra información específica del estudiante (polimorfismo)
        print(f"Nombre: {self._nombre} | Correo: {self._correo} | Rol: Estudiante | Carrera: {self._carrera}")


class Instructor(Usuario):
    # Subclase que representa a un instructor

    def __init__(self, nombre, correo, especialidad):
        # Inicializa los atributos heredados y agrega especialidad
        super().__init__(nombre, correo)
        self._especialidad = especialidad  # Área en la que el instructor enseña

    def mostrar_info(self):
        # Muestra información específica del instructor (polimorfismo)
        print(f"Nombre: {self._nombre} | Correo: {self._correo} | Rol: Instructor | Especialidad: {self._especialidad}")