import unittest
import database as db
import copy
import helpers
import config
import csv

class TestDatabase (unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('93G','Carlos','Rivas'),
            db.Cliente('65K','Isidro','Otero'),
            db.Cliente('27M','Xana','Rodriguez')
        ]

    def testBuscarCliente(self):
        clienteExistente=db.Clientes.buscar('93G')
        clienteInexistente=db.Clientes.buscar('00X')
        self.assertIsNotNone(clienteExistente)
        self.assertIsNone(clienteInexistente)

    def testCrearCliente(self):
        nuevoCliente = db.Clientes.crear('41T','Aitor','Correa')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(nuevoCliente.dni,'41T')
        self.assertEqual(nuevoCliente.nombre,'Aitor')
        self.assertEqual(nuevoCliente.apellido,'Correa')

    def testModificarCliente(self):
        clienteAModificar = copy.copy(db.Clientes.buscar('65K'))
        clienteModificado = db.Clientes.modificar('65K', 'Jorge', 'Otero')
        self.assertEqual(clienteAModificar.nombre, 'Isidro')
        self.assertEqual(clienteModificado.nombre, 'Jorge')

    def testBorrarCliente(self):
        clienteBorrado = db.Clientes.borrar('65K')
        clienteRebuscado = db.Clientes.buscar('65K')
        self.assertEqual(clienteBorrado.dni, '65K')
        self.assertIsNone(clienteRebuscado)

    def testDniValido(self):
        self.assertTrue(helpers.dniValido('99A',db.Clientes.lista))
        self.assertFalse(helpers.dniValido('36363636H',db.Clientes.lista))
        self.assertFalse(helpers.dniValido('F16',db.Clientes.lista))
        self.assertFalse(helpers.dniValido('93G',db.Clientes.lista))

    def testEscrituraCsv(self):
        db.Clientes.borrar('65K')
        db.Clientes.borrar('93G')
        db.Clientes.modificar('27M','Angela','Garces')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni,'27M')
        self.assertEqual(nombre,'Angela')
        self.assertEqual(apellido,'Garces')