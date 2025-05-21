"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    counts = {}
    
    with open('files/input/data.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            # 1) Separa las entradas "xxx:NN" de la columna 5
            partes = row[4].split(',')
            # 2) Para cada parte extrae sólo la clave (las tres letras)
            for entry in partes:
                clave = entry.split(':')[0]
                # 3) Incrementa el conteo de esa clave
                counts[clave] = counts.get(clave, 0) + 1

    return dict(sorted(counts.items()))

resultado = pregunta_09()
print(resultado)