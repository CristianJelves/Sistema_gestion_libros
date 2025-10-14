from funciones import (
    registrar_libro,
    registrar_usuario,
    consultar_libros,
    realizar_prestamo,
    listar_prestamos,
)

def mostrar_menu():
    # Muestra el menú de opciones
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Consultar libros")
    print("4. Realizar préstamo")
    print("5. Listar préstamos")
    print("6. Salir")

def ejecutar_sistema():
    # Bucle principal del sistema
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            consultar_libros()
        elif opcion == "4":
            try:
                realizar_prestamo()
            except Exception as e:
                print("Error:", e)
        elif opcion == "5":
            listar_prestamos()
        elif opcion == "6":
            print("Gracias por usar el sistema")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el sistema
ejecutar_sistema()