"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv 

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    valores = {}
    
    with open('files/input/data.csv') as f:
        reader = csv.reader(f, delimiter='\t')
        
        for row in reader:
            clave = int(row[1])
            letra = row[0]
            if clave not in valores:
                valores[clave] = set()
            valores[clave].add(letra)

    resultado = []
    for clave in sorted(valores):
        lista_letras = sorted(valores[clave])
        resultado.append((clave, lista_letras))
    return resultado

resultado = pregunta_08()
print(resultado)