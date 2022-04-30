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

