from numpy import conj, mat


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

    ## los conjuntos o sets son una bolsa
    # no tienen un orden
    # los conjuntos no tienen duplicados
    # los conjuntos no se indexan
    # 
    conjunto1 ={1,2,3,4, 'Edu', 'Edu', (1,2), (1,2)}
    print(conjunto1)

    #conjunto vacio; heterogeno ==> acepta diferentes tipos de datos pero que sean inmutables
    # No acepta otros conjuntos
    conjunto2=set()
    print(conjunto2)

    conjunto1 ={1,2,3,4, 'Edu', 'Edu', (1,2), (1,2), [12,3,4]}
    conjunto1 ={1,2,3,4, 'Edu', 'Edu', (1,2), (1,2), conjunto2}
    # no acepta otros conjuntos, ni listas, ni diccionarios como dato


    lista =[1,2,3,2,3,4,3,4,2,5]
    conjunto = set(lista)
    # crea un conjunto con los numeros no repetidos
    type(conjunto)
    print(conjunto)
    print(lista)

    #elimino los duplicados de una lista
    lista_no_duplicados = list(set(lista))
    print(lista)
    print(lista_no_duplicados)


    conjunto3 = set('hola mundo')
    print(conjunto3)

    conjunto4 = set(range(10))
    print(conjunto4)

    #Funciones del tipo de dato set
    #add agrega elementos a la lista
    conjunto1.add('Jose')
    print(conjunto1)

    conjunto1.add('Jose')
    print(conjunto1)

    #agregar varios elementos
    elementos = ['HOLAAA', 2,3,4,4]
    conjunto1.update(elementos) #acepta listas y cadenas
    print(conjunto1)

    elementos2 =[223,3,3,4,4,'pepe']
    for elemento in elementos2:
        conjunto1.add(elemento)

    print(conjunto1)


    conjunto1={1,2,3,5}
    conjunto1.update(range(11))
    print(conjunto1)
    

    #len()
    print(len(conjunto1))

    #discar() quita el elemento del conjunto
    conjunto1.discard(3)
    print(conjunto1)

    #remove falla si no puede eliminar el elemento
    conjunto1.remove(3)
    print(conjunto1)

    # in (para saber si un elemento está o no en un conjunto)
    print(3 in conjunto1)
    print(8 in conjunto1)

    print(conjunto1)

    eliminado = conjunto1.pop() #elimina aleatoriamente
    print(conjunto1)
    print(eliminado)

    #Elimina todo el contenido de un conjunto
    conjunto1.clear()
    print(conjunto1)



    usuarios = {"Miguel", "Blanca", "Mario", "Andrés"} 
    add_usuarios = ['Ana', 'Ramon', 'Marta', 'Eric', 'David']
    delete_usuarios =['Mario', 'Miguel', 'Esteban']
    print('Conjunto de usuarios inicial:')
    print(usuarios)

    usuarios.update(add_usuarios)
    print('Conjunto de usuarios update:')
    print(usuarios)

    print('Conjunto de usuarios delete:')
    for usuario in delete_usuarios:
        usuarios.discard(usuario)

    print(usuarios)


#Diccionario (coleccion no ordenada de objetos):
# Conjuntos clave:valor
diccionario1={'Nombre':'Eduardo', 
              'Edad':33,
              'notas':[10,10,9,10],
              'Apodo': 'Eduardo',
              0:'es un cero'
              }
print(diccionario1['Nombre'])
print(diccionario1['notas'])
print(diccionario1[0])

# similar al dataframe
type(diccionario1)
diccionario1['Edad']='Eduardo'
print(diccionario1)
diccionario1['Otro Apodo'] ='Lalo'
print(diccionario1)
diccionario1[' '] ='Otra cosa'
print(diccionario1)


diccionario2 = {}
diccionario2['clave']='valor'
diccionario2['otra']=12234

print(diccionario2)

diccionario2.update({'Altura':1.86, 'Peso':78})
print(diccionario2)

#####################################################
#####################################################
print(len(diccionario2))

## eliminar elemento de un diccionario
del diccionario2['Altura'] #elimina de una en una
print(diccionario2)

#######################################################
### in 
#######################################################

'clave' in diccionario2 # busca la clave

diccionario2['otra']=12234
print(diccionario2)
valor_borrado = diccionario2.pop('otra')
print(diccionario2)
print(valor_borrado)



diccionario3 = {'primero':3, 'segundo':45}
diccionario3['primero']+=8
print(diccionario3)



diccionario4 = {'Curso': 'Python', 'Comision':3760, 'Aprobados':'todos'}

for elemento in diccionario4: #devuelve las claves no el valor
    print(f'{elemento}:')
    print(f'{diccionario4[elemento]}')


llaves = diccionario4.keys() #devuelve una lista de llaves
values = diccionario4.values() #devuelve una lista de valores

print(llaves)
print(values)

for valor in diccionario4.values():
    print(f'Valor: {valor}')



for llave in diccionario4.keys():
    print(f'Clave: {llave}')

diccionario4.items() #lista de tuplas

for elemento in diccionario4.items():
    print(elemento)


for clave, valor in diccionario4.items():
    print(f'Clave: {clave}; Valor {valor}')

diccionario4.items()


lista = ['Eduardo', 'Montero', 'Bermudez']
for ubicacion, elemento in enumerate(lista):
    print(ubicacion)
    print(elemento)

############
# Desafio
############

animales ={'elefante':''}
otra_lista ={'perro':'Bobby', 'tigre':'Peepe', 'mono':'homero'}
animales.update(otra_lista)
print(animales)

animales['elefante']='Trompis'
animales['delfin'] ='Manolo'
print(animales)


####################################
## Metodos de colecciones
####################################

cadena1 = "Python en coder"
cadena_mayus = cadena1.upper()
print(cadena_mayus)
print(cadena1)

cadena1 = "Python en coder"
cadena1 = cadena1.lower()
print(cadena1)

cadena2 = "SoMos la comIsiOn 27620"
cadena2=cadena2.capitalize()
print(cadena2)

cadena3 = "SoMos la comIsiOn 27620"
cadena3=cadena3.title()
print(cadena3)

print(cadena3.count('7')) # cuenta cuantos 7 hay
print(cadena3.count('o')) # cuenta cuantos o hay
print(cadena3.count('om')) # cuenta cuantos om hay

print(cadena3.find('o')) # el indice de la primera aparición del caracter buscado
                          # del primer caracter de la cadena buscada
# -1 del find significa que no encontró

print(cadena3.rfind('o')) # muestra el indice de la ultima aparición de la cadena

cadena4 = "muchos Aires pocos Aires Buenos Aires"
lista = cadena4.split('Aires')
lista

cadena4 = 'hola como estas soy edu y soy el profe de python en esta comision 37360'
lista = cadena4.split(' ')#corta por palabra
lista

cadena4 = 'hola como estas soy edu y soy el profe de python en esta comision 37360'
lista = cadena4.split()
lista #corta por palabra

cadena1 = 'Eduardo'
",".join(cadena1) # a cada caracter le añade ,
#"separador".join('cadena')

cadena = 'El mejor profe es Juan'
print(cadena.replace('Juan', 'Edu'))


cadena = '----El mejor profe es Juan----'    
print(len(cadena))
print(len(cadena.strip('-')))
print(cadena.strip('-')) # por defecto usa el espacio

#Otras funciones super útiles:

#isdigit()
#isalnum
#isalfa
#islower
#isupper
#istitle
#isspace
#startswith()
#endswith()

#########
# listas
#########

lista = [1,2,34,3,2]
lista.clear()
lista

lista = [1,2,34,3,2]
lista =[]
lista

lista = [1,2,34,3,2]
lista2 = [1,2,3,4,3,5]
lista3 = lista+lista2
lista3


lista = [1,2,34,3,2]
lista2 = [1,2,3,4,3,5]
print(lista)
lista.extend(lista2) # la asigna en la misma lista
print(lista)

lista = [1,2,34,3,2]
lista.insert(2,'Nuevo')
lista

lista = [1,2,34,3,2]
lista.insert(4,(1,2,3,2)) # inserta un elemento en la posición especificada
lista
lista.reverse()


lista = [1,2,4,3,2,5,34,3]
lista.sort()
print(lista)
lista.sort(reverse = True)
print(lista)


cadena = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

lista = cadena.split('&')

cadena_final = ''
for indice, cadena in enumerate(lista):
    if indice >0:
        #print('- '+cadena.capitalize())
        cadena_final = cadena_final+'- '+cadena.capitalize()+'.'+'\n'
    else:
        #print(cadena.capitalize()+'...')
        cadena_final = cadena_final+cadena.capitalize()+'...'+'\n'

cadena_final = cadena_final.replace('joe', 'Joe').replace('castiglione', 'Castiglione')
print(cadena_final)

#########################
#Sets o Conjuntos
########################

conj1 = {1,2,4, 'Fran'}
conj2 = {6, 'Pepe'}
conj3 = {1,2,4,'Fran', 8,11}

#conj4 = conj1 # asi es copia por referencia
conj4 = conj1.copy() # asi es copia por valor
print(conj4)

conj1.isdisjoint(conj3) # False si comparten elementos
conj1.isdisjoint(conj2) # True si no comparten elementos

conj1.issubset(conj3)
conj1.issubset(conj2)

conj3.issuperset(conj1)

conj4 = conj1.union(conj3)
print(conj4) # los elementos juntos sin repetir

conj4 = conj3.difference(conj1)
print(conj4) #lo que esta en uno que no esta en otro



conj1 = {1,2,4, 'Fran'}
conj2 = {6, 'Pepe'}
conj3 = {1,2,4,'Fran', 8,11}
conj3.difference_update(conj1)
print(conj3)

set1 = {1,2,3,7}
set2 = {3,4,5}

set1.intersection_update(set2)
print(set1)

#####################################
## Diccionarios
#####################################

diccionario ={'Nombre':'Eduardo',
              'Edad':36,
              'Altura':1.86
}

print(diccionario.get('Apellido', -9999))
print(diccionario.get('Edad', -9999)) # se usa para que no pinche si no encuentra la clave

diccionario.keys() # lista de las claves
diccionario.values() # lista de los valores
diccionario.items() # Tupla de clave valor

for clave, valor in diccionario.items():
    print(f'la clave es: {clave} y el valor es {valor}')


# Desafio:
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
#1. Borrar los elementos duplicado
lista_new = list(set(lista))
#2. Ordenar la lista de mayor a menor
lista_new.sort(reverse = True)
#3. Eliminar todos los numeros impares
lista_pares=[]
for elemento in lista_new:
    if elemento%2==0:
        lista_pares.append(elemento)
#4. Sumar todos los elmentos de la lista
sum(lista_pares)
#5. Añadir como primer elemento de la lista la suma realizada 
lista_pares.insert(0, sum(lista_pares))
#6. Devolver la lista modificada
print(lista_pares)
#7. Finalmente, después de ejecutar la función, comprueba que la suma de todos 
#   los números a partir del segundo, concuerda con el primer número de la lista
if lista_pares[0] == sum(lista_pares[1:]):
    print('Operación de suma correcta.')
else:
    print('Operación de suma equivocada.')




lista =['Hola', 'Eduardo', 'Montero']
','.join(lista)

################################
## Manejo de archivos y datos
################################
## Datos Persistentes:
    # Archivos
    # Datos

