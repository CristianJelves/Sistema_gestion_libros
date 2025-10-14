# funciones.py
from modulos.libro import Libro
from modulos.usuario import Estudiante, Instructor
from modulos.prestamo import Prestamo
from modulos.excepciones import (
    LibroNoDisponible,
    UsuarioNoRegistrado,
    PrestamoDuplicado,
)

# Almacenes principales
libros = []      # Lista de objetos Libro
usuarios = []    # Lista de objetos Estudiante / Instructor
prestamos = []   # Lista de objetos Prestamo


def registrar_libro():
    # Crea y guarda un nuevo libro
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    libros.append(Libro(titulo, autor, genero))
    print("Libro registrado.")


def registrar_usuario():
    # Crea y guarda un nuevo usuario
    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")
    tipo = input("Tipo de usuario (estudiante/instructor): ")

    if tipo == "estudiante":
        carrera = input("Carrera: ")
        usuarios.append(Estudiante(nombre, correo, carrera))
        print("Estudiante registrado.")
    elif tipo == "instructor":
        especialidad = input("Especialidad: ")
        usuarios.append(Instructor(nombre, correo, especialidad))
        print("Instructor registrado.")
    else:
        print("Tipo de usuario no válido.")


def consultar_libros():
    # Busca libros por autor, género o disponibilidad
    criterio = input("Buscar por (autor/género/disponible): ")

    resultados = []

    if criterio == "autor":
        autor = input("Autor a buscar: ")
        for libro in libros:
            if libro._autor == autor:
                resultados.append(libro)

    elif criterio == "género" or criterio == "genero":
        genero = input("Género a buscar: ")
        for libro in libros:
            if libro._genero == genero:
                resultados.append(libro)

    elif criterio == "disponible":
        for libro in libros:
            if libro.esta_disponible():
                resultados.append(libro)
    else:
        print("Criterio no válido.")
        return

    if resultados:
        print("\n--- Libros encontrados ---")
        for libro in resultados:
            libro.mostrar_info()
    else:
        print("No se encontraron resultados.")


def realizar_prestamo():
    # Registra un préstamo si todo es válido
    nombre_usuario = input("Nombre del usuario: ")
    titulo_libro = input("Título del libro: ")

    # Buscar usuario
    usuario_encontrado = None
    for u in usuarios:
        if u._nombre == nombre_usuario:
            usuario_encontrado = u
            break
    if usuario_encontrado is None:
        raise UsuarioNoRegistrado()

    # Buscar libro
    libro_encontrado = None
    for l in libros:
        if l._titulo == titulo_libro:
            libro_encontrado = l
            break
    if libro_encontrado is None:
        print("El libro no está registrado.")
        return

    # Validar disponibilidad
    if not libro_encontrado.esta_disponible():
        raise LibroNoDisponible()

    # Verificar préstamo duplicado
    for p in prestamos:
        if p._libro == libro_encontrado and p._usuario == usuario_encontrado:
            raise PrestamoDuplicado()

    # Crear y almacenar el préstamo
    nuevo_prestamo = Prestamo(libro_encontrado, usuario_encontrado)
    nuevo_prestamo.realizar_prestamo()
    prestamos.append(nuevo_prestamo)


def listar_prestamos():
    # Muestra todos los préstamos activos
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        print("\n--- Lista de préstamos ---")
        for p in prestamos:
            p.mostrar_info()