from persona import Persona

class Empleado(Persona):

    def __init__(self, nombre, apellido, edad, sueldo, cargo):
        super().__init__(nombre, apellido, edad)

        self.sueldo = sueldo
        self.cargo = cargo

    def mostrar(self):
        return f'{super().mostrar()} sueldo: {self.sueldo} y cargo: {self.cargo}'


empleado1 = Empleado('Eduardo', 'Montero', 34, 3000, 'data scientist')

print(empleado1.mostrar())
print(empleado1.esMayor())
