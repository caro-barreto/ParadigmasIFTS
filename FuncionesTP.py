import math

def calcular_disparo(coordX, coordY):
    disparo = math.sqrt((coordX)**2 + (coordY)**2)
    return disparo

def calcular_mejor_disparo(disp1, disp2, disp3):
    if disp1 < disp2 and disp1 < disp3:
        return disp1
    elif disp2 < disp1 and disp2 > disp3:
        return disp2
    elif disp3 < disp1 and disp3 < disp2:
        return disp3

def calcular_promedio_disparo(d1, d2, d3):
    return (d1 + d2 + d3)/3


def ordenarDicEdad(lista):
    intercambios = True
    pasada = len(lista) - 1
    cont = 0
    while pasada > 0 and intercambios:
        intercambios = False
        for i in range(pasada):
            cont += 1

            if lista[i]['edad'] > lista[i + 1]['edad']:
                intercambios = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

        pasada = pasada - 1

    return lista

def ordenarDicMejorDisparo(lista):
    intercambios = True
    numPasada = len(lista) - 1
    cont = 0
    while numPasada > 0 and intercambios:
        intercambios = False
        for j in range(numPasada):
            cont += 1
            if lista[j]['mejordisparo'] > lista[j + 1]['mejordisparo']:
                intercambios = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

        numPasada = numPasada - 1

    return lista


def PromedioGeneral(lista, diccionario):
    contadorpromedio = 0
    for diccionario in lista:
        contadorpromedio += diccionario['promediodisparo']
        total = contadorpromedio/len(lista)
    return total


def SuperiorPromedio(lista, diccionario, promedio):
    for diccionario in lista:
        if diccionario['promediodisparo'] > promedio:
            print(diccionario)
