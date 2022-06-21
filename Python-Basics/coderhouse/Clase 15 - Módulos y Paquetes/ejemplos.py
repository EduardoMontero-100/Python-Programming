# modulo de python para usar funciones del sistema
import sys
# escribo argumentos del sistema
#print(f'Hola {sys.argv[1]} cómo estás?')

#script que imprima una palabra, una cantidad de veces, pasada por parámetro
if len(sys.argv)!=3:
    print('Ingrese solo 2 parámetros')
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])

