from numpy import mat


cuenta = (8*5+4)/5
print(cuenta)
cuenta ='Hola mundo'
print(cuenta)
cuenta =3**2 ## 3 evalado al  cuadrado
print(cuenta)
cuenta =10/3
print(cuenta)
cuenta = 10//3 # guarda el resto
print(cuenta) 
cuenta = 10%3 # guarda el modulo
print(cuenta) 

'''
Esta es otra forma de comentario
'''

print('Hola mundo! Me dicen \'Fran\'' ) # caracter de escapes
print("Hola mundo! Me dicen 'Fran'" ) # caracter de escapes
print('Hola mundo')
print('Hola soy Eduardo \n\n\n\nSoy el profesor de Python')
print('Hola soy Eduardo \tSoy el profesor de Python')

print('C:\\nome\eduardo\media') # no hace el salto de linea
print(r'C:\nome\eduardo\media') #raw (imprime como esta)
print(f'la suma de 3 +5 es: {3+5}')    #preprocesado/formatea lo que esta entre llaves y lo devuelve
print(f'El resultado de 8*5 es: {8*5}')
print(f'Vamos que se puede tu puntaje es \t {10*10}%')

suma = 3 +5
print(suma)

nombre_de_cajita = 'esto guardo en la cajita'
print(nombre_de_cajita)

variable_nueva = 'Hola' ## snake_case
fecha_de_nacimiento = "23 de mayo"
FechaDeNacimiento = 20220201 ## CamelCase
print(variable_nueva)
imc = 22
print(imc)
#Python es case sensitive
fecha_nacimiento=11
print(fecha_nacimiento)

#input
nombre = input('Ingrese su nombre')
print(nombre)
print(f'Su nombre es: {nombre}')

altura = 1.80
peso = 80
imc = peso/1.80**2

print(f'Tu imc es: {imc}')


cadena1 = 'Hola'
cadena2 = 'mundo'
concatenacion = cadena1+" "+cadena2
print(concatenacion)


cadena1 = 'moderno'
cadena2 = 'Python'
cadena3 = 'es un lenguaje'
cadena4 = 'de programación'

frase = cadena2+' '+cadena3+' '+cadena4+' '+cadena1
print(frase)
print(cadena2[2])
print(cadena2[-1])
print(len(cadena4))

##################
## Slicing
##################
cad = "Esto es un monton de cosas"
print(cad[0:8:1]) #  vamos desde 0 hay antes de 5 y saltamos de 1 en 1
print(cad[0:10:2]) 


cad= 'CadenaDeTextoParaJugar'
print(cad[20:0:-1]) # saca la cadena al reves

ejercicioSlicing = "acitametaM ,5.8 ,otipeP ordeP"
cadena_invertida = ejercicioSlicing[::-1]
print(cadena_invertida)

nombre = cadena_invertida[0:5:1]
print(nombre)
print(cadena_invertida)
# el apellido es Pepito

for i in my_list:
    print(i)

# listas:

lista_string = ["Hola", "como", "estas"]
lista_cadena = ["H","o", "l", "a", "", "m","u","n","d","o"] 
lista_numerica = [1,2,7,4, 23, 0]
lista_heterogenea =[1,2,3,"hola",4]
lista_nueva=[12, "chao", input("ingrese el tercer elemento")]
print(lista_nueva)

print(lista_numerica[4])
print(lista_string[2])
print(lista_cadena[0:4])
print(lista_heterogenea)
print(lista_heterogenea[-1])

#concatenar listas
lista_1 = ["hola", "coder", 23]
lista_2 =[9, ",mm", "fran"]

lista_nueva = lista_1 +lista_2
lista_nueva = lista_2 +lista_1
lista_nueva

#strings
lista_cadena = ["Hola", 35, "como", "coder", "house", 3,4,5,2,2]
lista_cadena[0]=93
print(lista_cadena)

#slicing
lista_cadena[4:8] #tomo desde la posición 4 hasta la 8
lista_cadena[:4]
print(lista_cadena[0:7:2])

# Añadir elementos al final de la lista con slicing
nueva_lista =[1,9,4,6]
print(nueva_lista)
nueva_lista[-1:]=[nueva_lista[-1], "coder",4,3,2,3]
nueva_lista

lista = [4,53,4,3,333,3322]
print(lista)
lista[-1:]=[lista[-1], "n1","n2", "n3"]
print(lista)

#Borrar con slicing
nueva_lista = [0,1,2,3,4,5,6,7,8,9]
print(nueva_lista)
nueva_lista[3:7] = []
print(nueva_lista)

#otra forma de borrar
print(nueva_lista)
nueva_lista=[]
print(nueva_lista)

# listas anidadas
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(matriz[2][0])

#metodos de listas
#append
lista=[]
lista.append("chao")
lista.append(9)
lista.append("hola")
print(lista)
lista.append(matriz)
print(lista)
len(lista)
len("eudjhjhdkhasdkljadads")
len([])

mi_lista_numerica =[1,2,3,3,33,2,2,2,444]
mi_lista_numerica.pop() # pop elimina el elemento en la ultima posicion
mi_lista_numerica
nueva_variable = mi_lista_numerica.pop() # pop guardo el ultimo elemento
nueva_variable

mi_lista_numerica.pop(4)
mi_lista_numerica
nueva_variable = mi_lista_numerica.pop(4)
nueva_variable

mi_lista_numerica =[1,2,3,3,33,2,2,2,444]
mi_lista_numerica.count(2) #count()cuenta la cantidad de elementos iguales respecto al elemento que se paso por parametro
mi_lista_numerica.index(2) # en que posicion esta el elemento pasado por parametro
sum(mi_lista_numerica) # suma los elementos de la lista

# Tuplas: #inmutables

tupla1 = (1,-5,64,3)
print(tupla1)
tupla2 = (111,22,3,4,5,5)
tupla_concat = tupla1+tupla2
print(tupla_concat)
# no funciona el append
# no se puede appendear tuplas con listas
print(tupla1 +[2,3,1,1])
tupla1=()
print(tupla1)# borra tupla

tupla1 = (2,)
print(tupla1) # tupla de 1 elemento
type(tupla1)
tupla1 = (2)
type(tupla1)
# las tuplas no tienen ni append ni pop
tupla1 =(2,3,2,1,2,2222,2,3)
print(tupla1)
lista = list(tupla1)
print(lista)
lista.append("Hola como estan")
print(lista)
type(lista)
convert_tupla = tuple(lista)
print(convert_tupla)
type(convert_tupla)

#sort() ordena de menor a mayor tienen que ser del mismo tipo
lista = [1,2,3,542,1,3]
lista.sort()
print(lista)

#reverse() ordena de mayor a menor tienen que ser del mismo tipo
lista.reverse()
print(lista) 
########################
## Desafio de Listas
########################
# hay mas opciones
# Ejercicios de listas:
# Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:
# Añade a la LISTA1 el int 1234 y luego el string “Hola”
# Añade a la LISTA2 el string “Adios” y luego el int 1234
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]
lista1.append(1234)
lista1.append('Hola')
lista2.append('Adios')
lista2.append(1234)
lista3= lista1[0:len(lista1)-1]
lista4 = lista2[1:len(lista2)-1]
lista5 = lista4+lista3

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5) 
########################
# Desafio de tuplas:
########################
tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
#sorted(tupla)
print(tupla[-1])
print(len(tupla))
print(tupla.index(87))
print(list(tupla[-3:len(tupla)] ))
print(tupla[8])
print(tupla.count(7))
## Operadores y expresiones
# true
print(2+3==23+4)
print(5!=3*2)
print(5==3*2)
print(32>32)
print(45>11)
print("aaa"<"aaab") #esta en orden alfabetico

nombre = 'Coderhouse'
nombre2 = "Fran"
nombre3 = 'Valen'

print((len(nombre)== len(nombre2))  !=  (len(nombre2)== len(nombre3)))
print((len(nombre)== len(nombre2))  !=  (len(nombre2)== len(nombre3)-1))


expresiones =[
    False == True,
    10>=2*4,
    33/3 ==11,
    True>False,
    True*5 == 2.5*2
]

print(expresiones)

# Operadores Lógicos Not, Or, And
not True == False

2==4/2 and 5==3

a = "Hola"
a[-1]

# Operadores de asignación
edad_edu = 34
edad_edu = edad_edu +43
edad_edu =34
edad_edu+=4
edad_edu


edad=20
edad*=10
edad=20
edad**=2
edad


nota_1 = 10
nota_2 = 7
nota_3 = 4

nota_media = nota_1 *0.15 + nota_2*0.35 +nota_3 *0.5
print(nota_media)



variable = "Hola"
variable+="6"
print(variable)

edad_Francisco = 20
edad_Francisco-=5
edad_Francisco

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

matriz

numero = int(input('Ingrese numero\n'))

if numero%2==0:
    print('El numero ingresado es par')
    if numero>20:
        print('El numero es mayor a 20')
else:
    print('El numero ingresado es impar')

## Ciclos:


num =5 
while(num>0):
    print(num)
    num-=1
print('Termino el proceso')



entrada = input('ingrese salir').lower()
while(entrada!='salir'):
    if entrada !=1:
        break
    entrada = input('ingrese salir').lower()
    print('Tiene que ingresar salir')


print('Saliste del bucle')

lista1 =[1,2,3]
lista2 = lista1
lista1.append(4)
print(lista1)
print(lista2)
# para elementos complejos pasa eso. 
# esto es pasaje por referencia

matriz=[
[1,5,1],
[2,1,2],
[3,0,1],
[1,4,4]
]

for lista in matriz:
    lista.append(sum(lista))
    print(lista)

print(matriz)


lista = [5,6,7,8,9,10]
for indice, valor in enumerate(lista):
    print(f'El indice es: {indice} y el elemento es: {valor}')



lista = [5,6,7,8,9,10]
print(lista)
for indice, valor in enumerate(lista):
    lista[indice]=valor+5

print(lista)


nombre ='Eduardo Montero'
for letra in nombre:
    print(f'----->Imprimo letra {letra}')


for numero in range(0,100,1):
    print(numero)

print(list(range(0,10)))

lista = list(range(0,10))
print(lista)

for n in range(20, 2, -2):
    print(f'Numero: {n}')
    input('OK?')

lista_notas =[2,3,4,2,3,9,8,6]

lista_aprobadas=[]
for nota in lista_notas:
    if nota>=6:
        lista_aprobadas.append(nota)
print(lista_aprobadas)



pares=[]
impares=[]

numero =5
while numero!=0:
    numero = input('Ingrese numero: \n')
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)
if sum(pares) > sum(impares):
    print('Lista de pares es mayor a la de impares')
else:
    print('Lista de impares es mayor a la de pares')