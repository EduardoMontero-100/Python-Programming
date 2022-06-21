# modulo es un archivo con funciones

import sys

if len(sys.argv) == 3:
    print('Cantidad ok')
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    if isinstance(n1, int) and n1 in range(11) and isinstance(n2, int) and n2 in range(11):
        print('Numeros ok')
        if (n1 >= 4 and n1 <7) and (n2 >= 4 and n2 <7): 
            print('Aprobado debe rendir final')
        elif n1 >= 7 and n2 >= 7:
            print('Promocionado')
        else:
            print('Reprobado')
    else:
        print('Rango erroneo') 
else:
    print('Ingreso solo dos argumentos')