[README.md](https://github.com/user-attachments/files/23059145/README.md)
# Sistema de Gestión de Libros

## Descripción
Propósito: Gestionar libros, usuarios y préstamos desde consola usando Programación Orientada a Objetos (POO) en Python.  
Enfoque: Mantener el código simple, legible y fácil de extender.

## Objetivos
- Organización: Separar responsabilidades por clases y módulos.
- Confiabilidad: Validar operaciones y manejar errores comunes.
- Usabilidad: Ofrecer un menú de consola claro para registrar, listar y prestar.

## Funcionalidades
- Libros: Registrar, listar, consultar disponibilidad y cambiar estado (prestar/devolver).
- Usuarios: Registrar estudiantes/instructores y listarlos.
- Préstamos: Crear préstamos si el libro está disponible y el usuario está registrado.
- Validaciones: Evitar préstamos duplicados y reportar errores de forma explícita.
- Evidencias: Capturas en `capturas/` (si están disponibles en el repo).


## Requisitos
- Python: 3.10 o superior.
- SO: Windows, Linux o macOS.
- Dependencias: No requiere librerías externas (estándar de Python).

## Instalación Y Ejecución
1. Clonar:  
   `git clone https://github.com/CristianJelves/Sistema_gestion_libros.git`
2. Entrar al proyecto:  
   `cd Sistema_gestion_libros`
3. Ejecutar el programa:  
   - Windows: `python main.py`  
   - Linux/macOS: `python3 main.py`

## Uso Rápido
- Menú: Elegir opción para **registrar libros/usuarios**, **listar** o **realizar/devolver préstamos**.
- Flujo típico:
  1. Registrar un usuario.
  2. Registrar un libro.
  3. Realizar un préstamo (verifica disponibilidad y existencia del usuario).
  4. Devolver el libro cuando corresponda.

## Manejo De Errores
- Libro No Disponible: Se impide prestar si el libro ya está prestado.
- Usuario No Registrado: Se impide prestar si el usuario no existe.
- Préstamo Duplicado: Se evita crear un préstamo para un libro ya prestado.

## Hoja De Ruta (Mejoras Futuras)
- Persistencia: Guardar/cargar datos en JSON (libros, usuarios y préstamos).
- Búsquedas: Funciones para buscar por título/ID o correo de usuario.
- Validaciones: Normalización y verificación de duplicados.
- UX: Colores o pequeños formatos en consola para mensajes.
- Pruebas: Agregar tests unitarios y de integración.
