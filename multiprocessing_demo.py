import threading
import multiprocessing
import time

def tarea(nombre):
    print(f"Tarea {nombre} iniciada.")
    time.sleep(2)
    print(f"Tarea {nombre} finalizada.")


# Usando threading
h1 = threading.Thread(target=tarea, args=("Thread-1",))
h2 = threading.Thread(target=tarea, args=("Thread-2",))

print("Iniciando tareas con threading...")
h1.start()
h2.start()

h1.join()
h2.join()
print("Tareas con threading completadas.")

# Usando multiprocessing
p1 = multiprocessing.Process(target=tarea, args=("Process-1",))
p2 = multiprocessing.Process(target=tarea, args=("Process-2",))

print("Iniciando tareas con multiprocessing...")
p1.start()
p2.start()

p1.join()
p2.join()
print("Tareas con multiprocessing completadas.")