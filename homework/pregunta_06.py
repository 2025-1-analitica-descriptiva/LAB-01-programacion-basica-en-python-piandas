"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores = {}

    with open('files/input/data.csv') as f:
        reader = csv.reader(f, delimiter='\t')
        
        for row in reader:
            cadenas = row[4].split(',')
            for item in cadenas:
                clave, valor = item.split(':')
                valor = int(valor)
                
                if clave not in valores:
                    valores[clave] = [valor]
                else:
                    valores[clave].append(valor)
    resultado = []
    for clave in sorted(valores):
        lista_valores = valores[clave]
        maximo = max(lista_valores)
        minimo = min(lista_valores)
        resultado.append((clave, minimo, maximo))
        
    return resultado

resultado = pregunta_06()
print(resultado)

            