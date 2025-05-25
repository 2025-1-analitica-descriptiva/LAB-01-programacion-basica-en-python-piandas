"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    
    resultado = {}

    with open('files/input/data.csv', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            clave = row[0]
            partes = row[4].split(',')                     
            valores = [int(p.split(':')[1]) for p in partes] 
            fila_sum = sum(valores)                 

            if clave in resultado:
                resultado[clave] += fila_sum
            else:
                resultado[clave] = fila_sum

    return {k: resultado[k] for k in sorted(resultado)}

resultado = pregunta_12()
print(resultado)