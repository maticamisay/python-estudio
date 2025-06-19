# 2. Leer 15 números y generar un arreglo con los primeros 8 números mayores que 20.
# Si no hay 8 números que cumplan la condición, repetir el primero hasta completar
# el arreglo. Si ningún número era mayor que 20, mostrar mensaje y salir.
# a. Calcular el promedio de los números que no entraron en el arreglo.
# b. Buscar el máximo elemento y mostrar el elemento que esté en la posición
# anterior.
# c. Mostrar el factorial de los elementos de posición par del arreglo.
import math
arrayNumeros=[]
arrayNoEntraron=[]

def leerNumerosHastaOcho(array,arrayDos):
    mayores = []
    no_mayores = []
    for i in range(15):
        numero = int(input(f"Ingrese el número {i+1}: "))
        while numero < 0:
            print("El número debe ser positivo. Intente nuevamente.")
            numero = int(input(f"Ingrese el número {i+1}: "))
            
        if numero > 20 and len(mayores)<8:
            mayores.append(numero)
        else:
            no_mayores.append(numero)
    
    if not mayores:
        print("No se ingresaron números mayores que 20.")
        return False
    
    while len(mayores) < 8:
        mayores.append(mayores[0])
    
    array.extend(mayores)
    arrayDos.extend(no_mayores)
    return True

def calcularPromedio(array):
    if not array:
        return 0
    return sum(array) / len(array)

# b. Buscar el máximo elemento y mostrar el elemento que esté en la posición
# anterior.
def encontrarMaximoAnterior(array):
    if len(array) < 2:
        return None  # No hay elemento anterior al máximo

    max_idx = 0
    for i in range(1, len(array)):
        if array[i] > array[max_idx]:
            max_idx = i

    if max_idx == 0:
        return None  # El máximo está en la primera posición, no hay anterior

    return array[max_idx - 1]
    
def factorialPosicionesPares(array):
    print("Factoriales de elementos en posiciones pares (0,2,4...):")
    for i in range(0, len(array), 2):
        print(f"Posición {i}: {array[i]}! = {math.factorial(array[i])}")
# factorial sin math
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorialSinMath(array):
    print("Factoriales de elementos en posiciones pares (0,2,4...) sin math:")
    for i in range(0, len(array), 2):
        print(f"Posición {i}: {array[i]}! = {factorial(array[i])}")

leerNumerosHastaOcho(arrayNumeros,arrayNoEntraron)
promedio = calcularPromedio(arrayNoEntraron)
maximo_anterior = encontrarMaximoAnterior(arrayNumeros)
print("Arreglo de mayores que 20:", arrayNumeros)
print("Números que no entraron:", arrayNoEntraron)
print("Promedio de los que no entraron:", promedio)
if maximo_anterior is not None:
    print("Elemento anterior al máximo:", maximo_anterior)
else:
    print("No hay elemento anterior al máximo.")
factorialPosicionesPares(arrayNumeros)
