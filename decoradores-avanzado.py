def agregar_metodo_hablar(cls):
    def hablar(self, mensaje):
        print(f"dice: {mensaje}")
    
    cls.hablar = hablar
    return cls

@agregar_metodo_hablar
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    

p = Persona("Juan", 30)
print(p.saludar())
p.hablar("¡Buenos días a todos!")