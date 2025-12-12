import time
#Programación Funcional Avanzada en Python — Decoradores Avanzados
#(decoradores, closures, funciones de orden superior)


# def funcion_externa(x):
#     # Variable local de la función externa
#     def funcion_interna(y):
#         # La función interna accede a 'x'
#         return x + y
#     # La función externa devuelve la función interna
#     return funcion_interna

# # Creamos un closure: 'sumar_diez' ahora es una función que siempre suma 10
# sumar_diez = funcion_externa(10)

# # Llamamos a la función interna a través del closure
# print(sumar_diez(5))  # Salida: 15 (porque recuerda el x=10)
# print(sumar_diez(3))  # Salida: 13


def contador_llamadas(func):
    contador = 0

    def wrapper(*args, **kwargs):
        nonlocal contador
        contador += 1
        print(f"La función '{func.__name__}' ha sido llamada {contador} veces.")
        return func(*args, **kwargs)

    return wrapper

@contador_llamadas
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")
saludar("Carlos")


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"Tiempo de ejecución de '{func.__name__}': {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def proceso():
    time.sleep(1)  # Simula una operación que toma tiempo

proceso()

#Decorador con argumentos
def permiso_requerido(permiso):
    def decorador(func):
        def wrapper(usuario, *args, **kwargs):
            if permiso in usuario.get("permisos", []):
                return func(usuario, *args, **kwargs)
            else:
                print(f"Acceso denegado para el usuario {usuario['nombre']}. Permiso '{permiso}' requerido.")
        return wrapper
    return decorador

@permiso_requerido("admin")
def eliminar_usuario(usuario, usuario_a_eliminar):
    print(f"Usuario {usuario_a_eliminar} eliminado por {usuario['nombre']}.")

usuario_admin = {"nombre": "AdminUser", "permisos": ["admin", "editar"]}
usuario_normal = {"nombre": "NormalUser", "permisos": ["ver"]}
eliminar_usuario(usuario_admin, "Usuario123")  # SI permitir


def log_llamadas(method):
    def wrapper(self, *args, **kwargs):
        print(f"Llamando al método '{method.__name__}' con argumentos {args} y {kwargs}")
        return method(self, *args, **kwargs)
    return wrapper

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    @log_llamadas
    def saludar(self, saludo):
        print(f"{saludo}, soy {self.nombre}.")

p = Persona("Luis")
p.saludar("Hola")

# metaprogramación
class MetaConRun(type):
    def __new__(cls, name, bases, attrs):
        if 'run' not in attrs:
            raise TypeError(f"La clase {name} debe definir un método 'run'.")
        return super().__new__(cls, name, bases, attrs)
    
class Aplicacion(metaclass=MetaConRun):
    def run(self):
        print("Aplicación corriendo...")

app = Aplicacion()
app.run()
""" 
Que enseña:
interceptar la creacion de clases
validacion automatica de metodos
control avanzado del modelo del objeto
"""
