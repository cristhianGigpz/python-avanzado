def contador():
    n = 1
    while n <= 10:
        yield n
        n += 1

gen = contador()
print(next(gen))  # Imprime 1
print(next(gen))  # Imprime 2
print(next(gen))  # Imprime 3

print("-------------------------")

# def contador_infinito():
#     n = 1
#     while True:
#         yield n
#         n += 1

# gen_infinito = contador_infinito()
# print(next(gen_infinito))  # Imprime 1
# print(next(gen_infinito))  # Imprime 2
# print(next(gen_infinito))  # Imprime 3
# print(next(gen_infinito))  # Imprime 4
# print(next(gen_infinito))  # Imprime 5

print("-------------------------")


def leer_lineas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()
    
for linea in leer_lineas('data.txt'):
    print(linea)

print("-------------------------")


numeros = [x * 2 for x in range(100)]
print(numeros[0])
print(numeros[1])
print(numeros[2])
print("-------------------------")
generador_numeros = (x * 2 for x in range(100))
print(next(generador_numeros))
print(next(generador_numeros))
print(next(generador_numeros))
print(next(generador_numeros))

def leer_numeros():
    for x in range(11):
        yield x

def pares(numeros):
    for numero in numeros:
        if numero % 2 == 0:
            yield numero
print("-------------------------")
for numero in pares(leer_numeros()):
    print(numero)