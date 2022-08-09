import csv
import config

class Cliente:

    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

class Clientes:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero,delimiter=';')
        for dni, nombre, apellido in reader:
            c = Cliente(dni, nombre, apellido)
            lista.append(c)

    @staticmethod
    def buscar(dni):
        for c in Clientes.lista:
            if c.dni==dni:
                return c

    @staticmethod
    def crear(dni,nombre,apellido):
        cliente = Cliente(dni,nombre,apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for ind,c in enumerate(Clientes.lista):
            if c.dni==dni:
                Clientes.lista[ind].nombre = nombre
                Clientes.lista[ind].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[ind]
    
    @staticmethod
    def borrar(dni):
        for ind,c in enumerate(Clientes.lista):
            if c.dni==dni:
                c = Clientes.lista.pop (ind)
                Clientes.guardar()
                return c

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH,'w', newline='\n') as fichero:
            writer = csv.writer(fichero,delimiter=';')
            for c in Clientes.lista:
                writer.writerow((c.dni,c.nombre,c.apellido))     
