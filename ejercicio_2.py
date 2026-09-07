#Pedir ncombre y saludar
nombre = input("¿Comó te llamas?")
print(nombre)
print("hola " + nombre)

#Crear lista
colores = ["rojo", "verde", "azul", "amarillo"]
print(colores) 

#Pedir edad y decir cuantos meses tengo

edad = int(input("¿cuantos años tienes?"))

meses = edad *12

print("tienes " + str(meses) + " meses")

num_1 = "5"
num_2 = "10"
Resultado_mal = num_1 + num_2
print("mal (concatenado):", Resultado_mal)
#El simbolo +  sirve para concatenar las cadenas de texto entre si
Resultado_bien = int (num_1) + int(num_2)
print("bien (suma):", Resultado_bien)

#Añadir y borrar una lista
asignatura = ["matematicas", "lengua", "Ingles"] 
#Añadir un elemento a la lista
asignatura.append("Teconologia")
print(asignatura)
#eliminar un eleemento de la lista
asignatura.remove("matematicas") #OJO si tienes un elemento con el mismo nombre, solo eliminara el primeor que se encuentre
print(asignatura)

#Enseñar las listas usando bucles
for a in asignatura:
    print("tu asignatura es:", a)

#Bucle while
palabra = ""
while palabra != "aura":
    palabra = input("escribe algo: ")
    if palabra != "aura":
        print("No haz farmeado suficiente aura xd")
print("has ganado aura xd")

#ejercicio 
numeros = int(input("introduce numeros:"))

while numeros !=0:
    print(numeros)
    if numeros >0:
        print(numeros)
print("Has terminado")
