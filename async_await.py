import asyncio
import time
#from time import sleep

async def tarea_larga(nombre:str, duracion:int) -> str:
    inicio = time.perf_counter()
    print(f"Tarea {nombre} iniciada, durará {duracion} segundos.")
    await asyncio.sleep(duracion)
    print(f"Tarea {nombre} finalizada.")
    fin = time.perf_counter()
    print(f"Tiempo de ejecución de {nombre}: {fin - inicio:.2f} segundos")
    return f"Resultado despues de  {duracion} segundos"


async def main() -> None:
    inicio_total = time.perf_counter()
    print("Inicio de tareas sincrónicas")
    resultados = await asyncio.gather(tarea_larga("A", 5), tarea_larga("B", 2), tarea_larga("C", 1))
    fin_total = time.perf_counter()
    print(f"Tiempo total de ejecución sincrónica: {fin_total - inicio_total:.2} segundos")
    print("Resultados:", resultados)

asyncio.run(main())

"""
import time
from time import sleep

def tarea_larga(nombre:str, segundos: int) -> str:
    inicio = time.perf_counter()
    print(f"Iniciando {nombre} larga de {segundos} segundos...")
    sleep(segundos)
    print(f"Tarea {nombre} completada.")
    fin = time.perf_counter()
    print(f"Tiempo de ejecución de {nombre}: {fin - inicio:.2f} segundos")
    return f"Resultado después de {segundos} segundos"


def main()-> None:
    inicio_total = time.perf_counter()
    print("Iniciando programa principal...")
    resultados = [tarea_larga("Tarea 1", 5), tarea_larga("Tarea 2", 3), tarea_larga("Tarea 3", 4)]
    print("Programa principal completado.")
    fin_total = time.perf_counter()
    print(f"Tiempo total de ejecución: {fin_total - inicio_total:.2f} segundos")
    print("Resultados:", resultados)

main()
"""

