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
                                
mi_perro = Perro('Pepe', 'bulldog', 8)
tu_perro = Perro('Jose', 'french', 4)

## Restar el kernel de python:
##%load_ext autoreload
##%autoreload 2


class Persona:
    # Atributos de clase
    especie = 'mamifero'
    raza = 'humana'
    __sueldo = 2000 #privado

    # Atributos de instancia
    def __init__(self, edad, nombre, apellido, profesion, perro) -> None:
        self.nombre = nombre
        self.__apellido = apellido
        self.edad = edad
        self.profesion = profesion
        self.perro = perro



    # Metodos 
    def _soy_feliz(self):
        return 'No les importa'

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


mi_persona = Persona(24, 'Edu', 'Montero','Ingeniero', mi_perro)
tu_persona = Persona(25, 'Luisa', 'Bermudez','Arquitecta', tu_perro)
    
############################
#Una persona tiene un perro
############################

print(mi_persona.perro)
print(mi_persona.edad)



################################# 
# Encapsulamiento:
# metodos y atributos privados
################################# 




