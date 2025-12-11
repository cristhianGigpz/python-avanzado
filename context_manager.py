import time

class Persona:
    def __init__(self, name):
        self.name = name
        

    def __str__(self):
        return f"Persona: {self.name}"
    
    def __repr__(self):
        return f"Persona(name={self.name!r})"


p = Persona("Juan")
print(p)  # Output: Persona: Juan
print(repr(p))  # Output: Persona(name='Juan')

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - S/ {self.precio}"

    def __repr__(self):
        return f"Producto({self.nombre!r}, {self.precio})"

    def __add__(self, otro):
        return self.precio + otro.precio

    def __eq__(self, otro):
        return self.precio == otro.precio

    def __bool__(self):
        return self.precio > 0

p1 = Producto("Laptop", 3500)
p2 = Producto("Celular", 1200)

print(p1 + p2)     # 4700
print(p1 == p2)    # False
print(bool(p1))    # True
print(p1)          # Laptop - S/ 3500

class Grupo:
    def __init__(self, miembros):
        self.miembros = miembros

    def __len__(self):
        return len(self.miembros)
    
    def __getitem__(self, index):
        return self.miembros[index]
    
    def __setitem__(self, index, value):
        self.miembros[index] = value
    
    def __iter__(self):
        return iter(self.miembros)
    
    def __next__(self):
        return next(self.miembros)

g = Grupo(["Juan", "Ana", "Luis"])
print(len(g))
print(g[1])  # Ana
g[1] = "Maria"
print(g.miembros)  # ['Juan', 'Maria', 'Luis']
for miembro in g:   
    print(miembro)

class ArchivoDemo:
    def __enter__(self):
        print("Abriendo archivo...")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Cerrando archivo...")

with ArchivoDemo():
    print("Trabajando con el archivo...")


# with open("archivo_demo.txt", "x") as f:
#     f.write("Hola, mundo!")

class Cronometro:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        print(f"Tiempo transcurrido: {self.end - self.start:.4f} segundos")
        if exc_type:
            print(f"Ocurrió una excepción: {exc_value}")
        return True  # Maneja la excepción

with Cronometro():
    for _ in range(3):
        time.sleep(1)