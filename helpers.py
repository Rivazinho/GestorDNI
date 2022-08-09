import os
import re

def leerTexto(lonMin=0, lonMax=100, mensaje=None):
    if mensaje:
        print(mensaje)
    else: 
        None
    while True:
        texto = input("> ")
        if len(texto) >= lonMin and len(texto) <= lonMax:
            return texto

def dniValido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for c in lista:
        if c.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True

