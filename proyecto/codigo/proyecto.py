import urllib.request
from collections import deque

def linkArchivo():
    url = input()
    urllib.request.urlretrieve(url,"archivo.csv")

def leerArchivo():
    with open("archivo.csv", "r") as archivoCsv:
        codigo = archivoCsv.read()
        return codigo

def crearLista(codigo):
    lineas = codigo.split("\n")
    lista = deque()
    for linea in lineas:
        if linea != "":
            lista.insert(0, linea.split(","))
    return lista

def __main__():
    linkArchivo()
    codigo = leerArchivo()
    lista = crearLista(codigo)
    print(lista)

__main__()