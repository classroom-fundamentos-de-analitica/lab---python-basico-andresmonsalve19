"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
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
    letras = {}
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            letra = row[0]
            valor = int(row[1])
            if not letra in letras:
                letras[letra] = (valor, valor)
            else:
                letras[letra] = (max(valor, letras[letra][0]),
                                 min(valor, letras[letra][1]))
    result = sorted([(k, v[0], v[1]) for k, v in letras.items()])
    return result


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
    resultado_diccionario = {}
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            registros = row[4].split(",")
            for registro in registros:
                clave, valor = registro.split(":")
                valor = int(valor)
                if not clave in resultado_diccionario:
                    resultado_diccionario[clave] = (valor, valor)
                else:
                    resultado_diccionario[clave] = (min(valor, resultado_diccionario[clave][0]), max(
                        valor, resultado_diccionario[clave][1]))
    result = sorted([(k, v[0], v[1])
                    for k, v in resultado_diccionario.items()])
    return result


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
    associacion = {}
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            letra = row[0]
            numero = row[1]
            if not numero in associacion:
                associacion[numero] = [letra]
            else:
                associacion[numero].append(letra)
    result = sorted([(int(k), v) for k, v in associacion.items()])
    return result


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
    associacion = {}
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            letra = row[0]
            numero = row[1]
            if not numero in associacion:
                associacion[numero] = set(letra)
            else:
                associacion[numero].add(letra)
    result = sorted([(int(k), sorted(list(v)))
                    for k, v in associacion.items()])
    return result


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
    resultado_diccionario = {}
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            registros = row[4].split(",")
            for registro in registros:
                clave, _ = registro.split(":")
                if not clave in resultado_diccionario:
                    resultado_diccionario[clave] = 1
                else:
                    resultado_diccionario[clave] += 1
    return resultado_diccionario


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
    lista_resultado = []
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            tupla = (row[0], len(row[3].split(",")), len(row[4].split(",")))
            lista_resultado.append(tupla)
    return lista_resultado


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
    resultado_diccionario = {}
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            elementos = row[3].split(",")
            valor = int(row[1])
            for elemento in elementos:
                if not elemento in resultado_diccionario:
                    resultado_diccionario[elemento] = valor
                else:
                    resultado_diccionario[elemento] += valor

    return resultado_diccionario


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
    resultado_diccionario = {}
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            elementos = row[4].split(",")
            clave = row[0]
            for elemento in elementos:
                _, valor = elemento.split(":")
                valor = int(valor)
                if not clave in resultado_diccionario:
                    resultado_diccionario[clave] = valor
                else:
                    resultado_diccionario[clave] += valor
    return resultado_diccionario
