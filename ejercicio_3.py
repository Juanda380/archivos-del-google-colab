#numeros pares del 1 al 20
pares = []
for numero in range (1,21):
    if numero % 2 == 0:
        print("es un numero par")
        pares.append(numero)
print(pares)

#ejercicio 1
numeros = [5, 15, 8, 23, 6, 11]
mayores = []
for numeros in range (6,16):
    if numeros >= 10:
        mayores.append(numeros)
print(numeros)