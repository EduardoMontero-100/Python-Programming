class Persona:
    # Atributos de clase
    especie = 'mamifero'
    raza = 'humana'

    # Atributos de instancia
    def __init__(self, edad, nombre, profesion, perro) -> None:
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.perro = perro


    # Metodos 
    def get_edad(self):
        return self.edad
    
    def get_nombre(self):
        return self.nombre
    
    def get_profesion(self):
        return self.profesion

    def cumpleanos(self):
        print('Estoy cumpliendo años')
        self.edad +=1 

    #Metodo: Indica a la clase como se debe mostrar
    def __str__(self):
        return f'Yo, {self.nombre} soy una persona'
    
    #Metodo: Indica que tiene que devolver cuando se usa len sobre la instancia de la clase
    def __len__(self):
        return len(self.profesion)

    def horas_trabajadas(self, horas):
        print(f'Soy {self.nombre} y trabajo {horas} diarias')


