"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv 

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    resultado = []
    
    with open('files/input/data.csv', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            letra = row[0]
            elementos_col4 = row[3].split(',')  
            elementos_col5 = row[4].split(',')  

            cuenta4 = len(elementos_col4)
            cuenta5 = len(elementos_col5)

            resultado.append((letra, cuenta4, cuenta5))

    return resultado

resultado = pregunta_10()
print(resultado)