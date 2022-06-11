class Jugador:

    def __init__(self, nombre, apellido, perro) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__perro = perro

    #metodos get
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_perro(self):
        return self.__perro

    #metodos set
    def set_nombre(self, nombre):
        print('Cambie el nombre')
        self.__nombre = nombre

    def set_apellido(self, apellido):
        print('Cambie el apellido')
        self.__apellido = apellido

    def set_perro(self, perro):
        print('Cambie el perro')
        self.__perro = perro    


jugador1 = Jugador('Pepe', 'Contreras', 'Rufus')
jugador2 = Jugador('Luisa', 'Lopez', 'Coco')


print(jugador1.get_apellido())
print(jugador2.get_apellido())

jugador1.set_apellido('Montero')
jugador2.set_apellido('Constante')

print(jugador1.get_apellido())
print(jugador2.get_apellido())


