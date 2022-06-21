class Persona:

    especie = 'Humano'
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad

    # Se ejecuta cuando se hace un print al objecto
    def __str__(self):
        return f'{self.nombre} es una persona'

    def mostrar(self):
        return(f'Nombre: {self.nombre}; Apellido {self.apellido}; Edad {self.__edad}')

    def esMayor(self):
        if self.__edad > 18:
            resultado = 'Eres mayor de edad'
        else:
            resultado = 'Eres menor de edad'
        return resultado

    #getters and setters
    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad
        return 'Se modifico la edad'
            

persona1 = Persona('Eduardo', 'Montero', 34)
persona1.esMayor()
persona1.getEdad()
persona1.setEdad(32)
persona1.getEdad()

print(persona1)
persona1.mostrar()





