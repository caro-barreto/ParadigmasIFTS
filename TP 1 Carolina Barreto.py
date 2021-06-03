import csv
from FuncionesTP import *

id = input('Ingrese el número de participante')
db = []
while id != '999':
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese Apellido: ')
    edad = int(input('Ingrese edad: '))
    sexo = input('Ingrese F para femenino o M para masculino: ' )

    x1 = int(input('Ingrese la coordenada x del primer disparo '))
    y1 = int(input('Ingrese la coordenada y del primer disparo '))
    primer_disparo = calcular_disparo(x1, y1)

    x2 = int(input('Ingrese la coordenada x del segundo disparo '))
    y2 = int(input('Ingrese la coordenada y del segundo disparo '))
    segundo_disparo = calcular_disparo(x2, y2)

    x3 = int(input('Ingrese la coordenada x del tercer disparo '))
    y3 =int(input('Ingrese la coordenada y del tercer disparo '))
    tercer_disparo = calcular_disparo(x3, y3)

    mejor_disparo = float(calcular_mejor_disparo(primer_disparo, segundo_disparo, tercer_disparo))

    promedio_disparos = calcular_promedio_disparo(primer_disparo, segundo_disparo, tercer_disparo)

    participante = {
        'id': '',
        'nombre': '',
        'apellido': '',
        'edad': '',
        'sexo': '',
        'promediodisparo': '',
        'mejordisparo': ''
    }

    participante['id'] = id
    participante['nombre'] = nombre
    participante['apellido'] = apellido
    participante['edad'] = edad
    participante['sexo'] = sexo
    participante['promediodisparo'] = promedio_disparos
    participante['mejordisparo'] = mejor_disparo

    db.append(participante)
    id = input('Ingrese el número de participante')

print('Lista de participantes')
print(db)

with open('participantes.csv', 'w', newline='') as f:
    fieldnames = ['id','nombre', 'apellido','edad','sexo','promediodisparo','mejordisparo']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for participante in db:
        writer.writerow(participante)

resultado = ordenarDicMejorDisparo(db)
primerpuesto = str(resultado[0])
segundopuesto = str(resultado[1])
tercerpuesto = str(resultado [2])

print('Primer, segundo y tercer puesto:')
print(primerpuesto)
print(segundopuesto)
print(tercerpuesto)

with open('ganadores.csv', 'w', newline='') as g:
    fieldnames = ['id','nombre', 'apellido','edad','sexo','promediodisparo','mejordisparo']
    writer = csv.DictWriter(g, fieldnames=fieldnames)

    writer.writeheader()
    for participante in resultado[0:3]:
        writer.writerow(participante)

ultimopuesto = resultado[-1]
print(f'El ultimo puesto fue: {ultimopuesto}')


cantidad_participantes = len(db)
print(f'En el concurso hubo {cantidad_participantes} participantes')


"""A partir de acá lo había hecho originalmente con funciones, pero no conseguí manejar la lista de diccionarios de forma correcta, 
por lo que no lograba imprimir los datos necesarios, así que preferí hacerlo directamente así """


lista_hombres = []
for participante in db:
    if participante['sexo'] == 'M':
        lista_hombres.append(participante)
cantidad_hombres = len(lista_hombres)

print(f'Participaron {cantidad_hombres} hombres')

lista_mujeres = []
for participante in db:
    if participante['sexo'] == 'F':
        lista_mujeres.append(participante)

cantidad_mujeres = len(lista_mujeres)

for participante in db:
    if participante['sexo'] == 'F':
        edades_mujeres = [participante['edad'] for participante in lista_mujeres]

        edad_total_mujeres = 0
for edad in edades_mujeres:
    edad_total_mujeres += edad


edad_promedio_mujeres = edad_total_mujeres/cantidad_mujeres
print(f'La edad promedio de las mujeres es {edad_promedio_mujeres}')


orden_edad = ordenarDicEdad(db)
print('Participantes ordenados por edad')
print(orden_edad)

promTotal = PromedioGeneral(db, participante)
print(f'El promedio general de disparos es de {promTotal}')

print('Participantes con disparos por encima del promedio:')
encima_del_promedio = SuperiorPromedio(db, participante, promTotal)
