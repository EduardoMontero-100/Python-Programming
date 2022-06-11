class Perro:
    # Atributos de clase
    especie = 'mamifero'
    #Metodo: Constructor
    def __init__(self, nombre, raza, edad): 
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    #Metodo: Que indica a la clase como se debe mostrar
    def __str__(self):
        return f'Hola me llamo {self.nombre} y soy un perro'

    def ladrar(self):
        print('Estoy ladrando gua gua')

    def caminar(self, pasos):
        print(f'Hola soy el perro {self.nombre} y caminé {pasos} pasos')
                                
""" mi_perro = Perro('Pepe', 'bulldog', 8)
tu_perro = Perro('Jose', 'french', 4) """