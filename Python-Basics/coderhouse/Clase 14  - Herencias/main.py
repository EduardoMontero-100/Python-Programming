# Concepto de Polimorfismp
class Persona():

    def __init__(self) -> None:
        self.dni = 95423914

    def mensaje(self):
        print('Mensaje de la clase persona')

class Obrero(Persona):
    
    def __init__(self) -> None:
        self.__especialista = 1
    
    def mensaje(self):
        print('Mensaje de la clase obrero')

persona1 = Persona()
obrero1 = Obrero()

persona1.mensaje()
obrero1.mensaje()



def verMensaje(x):
    x.mensaje()

lista1 =[]
lista1.append(persona1)
lista1.append(obrero1)


for i in lista1:
    verMensaje(i)


## Polimorfismo o Duck Type
class Animal():
    def hablar(self):
        print('Soy un animal')

class Perro(Animal):
    def hablar(self):
        super().hablar()
        print('Gua Gua')

class Gato(Animal):
    def hablar(self):
        super().hablar()
        print('Miau')

class Pato(Animal):
    def hablar(self):
        super().hablar()
        print('Cuack')

class Persona():
    def hablar(self):
        print('Hola mundo')

perro1 = Perro()
gato1 = Gato()
pato1 = Pato()
persona1 = Persona()

lista = [perro1, gato1, pato1, persona1]

for i in lista:
    i.hablar()

