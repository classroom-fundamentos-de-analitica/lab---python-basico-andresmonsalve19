"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from io import open

file = open('data.csv', 'r')
data = file.readlines()
file.close()

print(data[0])


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """

    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()
    return sum(int(var.strip().split('\t')[1]) for var in datos)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [var.strip().split('\t')[0] for var in datos]
    col1 = sorted(dict.fromkeys(datos))
    respuesta = []
    [respuesta.append((x, datos.count(x))) for x in col1]

    return respuesta


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [var.strip().split('\t')[:2] for var in datos]
    col1 = sorted(list({var[0] for var in datos}))
    respuesta = []

    for letra in col1:
        sum = 0
        for camp in datos:
            if camp[0] == letra:
                sum += int(camp[1])
        respuesta.append((letra, sum))

    return respuesta


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [var.strip().split('\t')[2][5:7] for var in datos]
    col1 = sorted(dict.fromkeys(datos))
    respuesta = []
    [respuesta.append((x, datos.count(x))) for x in col1]

    return respuesta


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    letras = []
    colMax = []
    colMin = []
    maximos = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not row[0] in letras):
                letras.append(row[0])
                colMax.append(int(row[1]))
                colMin.append(int(row[1]))
            else:
                if(colMax[letras.index(row[0])] < int(row[1])):
                    colMax[letras.index(row[0])] = int(row[1])
                if(colMin[letras.index(row[0])] > int(row[1])):
                    colMin[letras.index(row[0])] = int(row[1])
    for letra in letras:
        maximos.append(
            (letra, colMax[letras.index(letra)], colMin[letras.index(letra)]))
    maximos.sort(reverse=False)
    return maximos


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    letras=[]
    colMax = []
    colMin = []
    dic = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for cod in row[4].split(','):
                letra = cod.split(':')[0]
                codigo = cod.split(':')[1]
                if(not letra in letras):
                    letras.append(letra)
                    colMax.append(int(codigo))
                    colMin.append(int(codigo))
                else:
                    if(colMax[letras.index(letra)]<int(codigo)):
                        colMax[letras.index(letra)]=int(codigo)
                    if(colMin[letras.index(letra)]>int(codigo)):
                        colMin[letras.index(letra)]=int(codigo)
    for letra in letras:
        dic.append((letra,colMin[letras.index(letra)],colMax[letras.index(letra)]))
    dic.sort(reverse=False)
    return dic


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    numeros = []
    letras = []
    reg = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not int(row[1]) in numeros):
                numeros.append(int(row[1]))
                letras.append([row[0]])
            else:
                letras[numeros.index(int(row[1]))].append(row[0])
    for numero in numeros:
        reg.append((numero, letras[numeros.index(numero)]))
    reg.sort(reverse=False)
    return reg


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    numeros = []
    letras = []
    reg = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not int(row[1]) in numeros):
                numeros.append(int(row[1]))
                letras.append([row[0]])
            else:
                if(not row[0] in letras[numeros.index(int(row[1]))]):
                    letras[numeros.index(int(row[1]))].append(row[0])

    for numero in numeros:
        order = letras[numeros.index(numero)]
        order.sort()
        reg.append((numero, order))
    reg.sort(reverse=False)
    return reg


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    columna = []
    letras = []
    dictionario = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for cod in row[4].split(','):
                letra = cod.split(':')[0]
                columna.append(letra)
                if(not letra in letras):
                    letras.append(letra)
    letras.sort()
    for letra in letras:
        dictionario.update({letra: columna.count(letra)})
    return dictionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    letras = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            col4 = row[3].split(",")
            col4 = len(col4)
            col5 = row[4].split(",")
            col5 = len(col5)
            letras.append((row[0], col4, col5))
    return letras


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    letras = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for letra in row[3].split(","):
                if(not letra in letras.keys()):
                    letras.update({letra: int(row[1])})
                else:
                    letras[letra] += int(row[1])
    dicc = sorted(letras.items())
    return dict(dicc)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    letras = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            letra = row[0]
            for codigo in row[4].split(","):
                numero = int(codigo.split(":")[1])
                if(not letra in letras.keys()):
                    letras.update({letra: numero})
                else:
                    letras[letra] += numero
    dicc = sorted(letras.items())
    return dict(dicc)


print(pregunta_12())
