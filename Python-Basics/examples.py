
from imp import NullImporter


def calcular_iva(precio):
    iva = precio * 0.21
    precio_iva = precio * 1.21
    return [iva, precio_iva]


precio_producto = 1000
nombre_producto = 'Lampara'

print(f'Nombre Producto: {nombre_producto}')
print(f'Precio Producto: {precio_producto}')
iva = calcular_iva(precio_producto)[0]
precio_iva = calcular_iva(precio_producto)[1]
print(f'Iva: {iva}')
print(f'Precio + Iva: {precio_iva}')
print(type(calcular_iva(precio_producto)))


def saludar(nombre:str): # es una pista sobre el tipo
    print(f'Bienvenido {nombre}')


saludar('Pepe')
saludar(100)

#Scope o entorno


def par_o_impar(x):
    if type(x) == int:
        if x%2==0:
            print('El número es par')
        else:
            print('El número es impar')
    else:
        print('Por favor ingrese un número')
        
par_o_impar(4.5)


#Funciones
def sum(x, y): #parametros
    return x + y  

sum(5,6) #argumentos

def maximo(numero1, numero2):
    print(numero1)
    print(numero2)
    if numero1>numero2:
        return numero1
    else:
        return numero2

maximo(5,44) # llamar a la función por posición (importa el orden)
maximo(numero2=5, numero1=44) # llamar a la función por nombre (no importa el orden)

def resta(numero1=0, numero2=0): # valores de parametros por defecto
    return numero1 - numero2

resta(6,3)

persona = {}
persona['nombre'] = input('Ingrese nombre \n')
persona['apellido'] = input('Ingrese apellido \n')
persona['edad'] = input('Ingrese edad \n')

print(f"Nombre { persona['nombre']}")
print(f"Apellido { persona['apellido']}")
print(f"Edad { persona['edad']}")

###########################################################################
###########################################################################

def duplicar(numer):
    numer *= 2
    return numer

numero =5
print('------------------')
print('------------------')

print(duplicar(numero))
print('------------------')
print(numero)

################################################
# Recursividad
################################################
# cuando una función se llama a sí misma

def cuenta_iterativa(numero):
    for i in range(1, numero+1):
        print(i)
cuenta_iterativa(8)



def cuenta(numero):
    numero -= 1
    if numero >= 0:
        cuenta(numero)
        print(f'---- {numero}')

cuenta(9)

# menos eficientes en cuento a memoria vs. funciones iterativas
def factorial(n):
    if n==0 or n==1:                # caso base no recursivo (cierre)
        return 1
    else:
        return n * factorial(n-1)   # caso recursivo


factorial(3)

###############################
#3 *factorial(2)
#    3 * 2 * factorial(1)
#        3 * 2 * 1
###############################

# Funciones Integradas
int() # convierte a entero
float() # convierte a float
str() # convierte a string
round() # redondea un float

help(int)