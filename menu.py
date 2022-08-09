import os
import helpers
import database as db

def iniciar():
    while True:
        os.system('cls')

        print("*////////////////////////")
        print("*       Bienvenido       ")
        print("*////////////////////////")
        print("*[1] Listar los clientes ")
        print("*[2] Buscar un cliente   ")
        print("*[3] Añadir un cliente   ")
        print("*[4] Modificar un cliente")
        print("*[5] Borrar un cliente   ")
        print("*[6] Cerrar el gestor    ")
        print("*////////////////////////")

        opcion = input("> ")
        os.system('cls')

        if opcion == '1':
            print("Listando los clientes...\n")
            for c in db.Clientes.lista:
                print(c)

        elif opcion == '2':
            print("Buscando un cliente...\n")
            dni = helpers.leerTexto(3, 3, "DNI (2 int y 1 char)").upper()
            c = db.Clientes.buscar(dni)
            if c:
                print(c)
            else:
                 print("Cliente no encontrado.")

        elif opcion == '3':
            print("Añadiendo un cliente...\n")
            dni = None
            while True:
                dni = helpers.leerTexto(3, 3, "DNI (2 int y 1 char)").upper()
                if helpers.dniValido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leerTexto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leerTexto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        elif opcion == '4':
            print("Modificando un cliente...\n")
            dni = helpers.leerTexto(3, 3, "DNI (2 int y 1 char)").upper()
            c = db.Clientes.buscar(dni)
            if c:
                nombre = helpers.leerTexto(2, 30, f"Nombre (de 2 a 30 chars) [{c.nombre}]").capitalize()
                apellido = helpers.leerTexto(2, 30, f"Apellido (de 2 a 30 chars) [{c.apellido}]").capitalize()
                db.Clientes.modificar(c.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '5':
            print("Borrando un cliente...\n")
            dni = helpers.leerTexto(3, 3, "DNI (2 int y 1 char)").upper()
            if db.Clientes.borrar(dni):
                print("Cliente borrado correctamente.") 
            else:
                print("Cliente no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")