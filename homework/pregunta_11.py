"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sums = {}

    with open('files/input/data.csv', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            valor = int(row[1])
            letras = row[3].split(',')
            for letra in letras:
                if letra in sums:
                    sums[letra] += valor
                else:
                    sums[letra] = valor
    return {k: sums[k] for k in sorted(sums)}

resultado = pregunta_11()
print(resultado)