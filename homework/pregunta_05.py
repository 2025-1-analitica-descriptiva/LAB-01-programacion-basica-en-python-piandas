"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    counts = {}
    
    with open('files/input/data.csv') as f:
        reader = csv.reader(f, delimiter='\t')
        
        counts = {}
        
        for row in reader:
            letra = row[0]
            valor = int(row[1])
            
            if letra not in counts:
                counts[letra] = [valor]
            else:
                counts[letra].append(valor)
                
    resultado = []
    for letra in sorted(counts):
        lista_valores = counts[letra]
        maximo = max(lista_valores)
        minimo = min(lista_valores)
        resultado.append((letra, maximo, minimo))
        
    return resultado

resultado = pregunta_05()
print(resultado)