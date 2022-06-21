class Mamifero:

    def __init__(self, cantidad_mamas, esperanza_vida) -> None:
        self.cantidad_mamas = cantidad_mamas
        self.esperanza_vida = esperanza_vida

    def mamar(self):
        print('Este animal mama')

    def nacer(self):
        print('Este animal nacio')


class AnimalMarino:

    def __init__(self, tiene_branqueas, especie) -> None:
        self.tiene_branqueas= tiene_branqueas
        self.especie = especie

    def nadar(self):
        print('Este animal nada')


class Cetaceo(Mamifero, AnimalMarino):
    
    def __init__(self, cantidad_mamas, esperanza_vida, tiene_branqueas, especie, notas, viveEn, peso ) -> None:
        super().__init__(cantidad_mamas, esperanza_vida)
        super().__init__(tiene_branqueas, especie)

        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso

    def nacer(self):
        super().nacer()

    def nadar(self):
        super().nadar()


# Indica la prioridad de ejecución de las clases
print(f'Orden de ejecución de los métodos {Cetaceo.__mro__} ') 
ballena = Cetaceo(True, 5, True,'Super Especie','Es grande', 'Galapagos', 20)
orca = Cetaceo(True, 5, True, 'Super Especie', 'Es pequeña', 'Argentina', 15)

ballena.nacer()
ballena.nadar()

