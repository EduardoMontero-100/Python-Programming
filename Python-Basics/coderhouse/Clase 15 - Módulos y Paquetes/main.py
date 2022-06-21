import sys
#import utils
from utils import multiplicar, sumar, restar

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print(f'La suma de {n1} mas {n2} es {sumar(n1,n2)}')
print(f'La resta de {n1} menos {n2} es {restar(n1,n2)}')
print(f'La multiplicacion de {n1} por {n2} es {multiplicar(n1,n2)}')

# hacer ejercicio pag 39
#paquete, modulo, funcion

