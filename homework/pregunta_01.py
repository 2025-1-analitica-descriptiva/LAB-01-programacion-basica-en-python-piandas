"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('files/input/data.csv') as f:
        reader = csv.reader(f, delimiter='\t')
        total = sum(int(row[1]) for row in reader)
    print(total)
    return total

pregunta_01()