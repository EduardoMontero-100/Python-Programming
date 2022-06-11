from persona import Persona
from perro import Perro



mi_perro = Perro('Osito', 'Bulldog', 4)
mi_persona = Persona(25, 'Eduardo','Ingeniero', mi_perro) 


print(mi_persona.get_edad())
print(mi_persona.get_profesion())
