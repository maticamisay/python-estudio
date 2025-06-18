# 2. Leer 15 números y generar un arreglo con los primeros 8 números mayores que 20.
# Si no hay 8 números que cumplan la condición, repetir el primero hasta completar
# el arreglo. Si ningún número era mayor que 20, mostrar mensaje y salir.
# a. Calcular el promedio de los números que no entraron en el arreglo.
# b. Buscar el máximo elemento y mostrar el elemento que esté en la posición
# anterior.
# c. Mostrar el factorial de los elementos de posición par del arreglo.

arrayNumeros=[]
arrayNoEntraron=[]

def leerNumerosHastaOcho(array,arrayDos):
    count = 0
    for i in range(15):
        while (count < 8 or i<15):
            numero = int(input(f"Ingrese el número {i+1}: "))
            i+=1
            if numero > 20:
                array.append(numero)
                count += 1
            else:
                arrayDos.append(numero)
    if count < 8:
        if array:
            primer_numero = array[0]
            while len(array) < 8:
                array.append(primer_numero)
        else:
            print("No se ingresaron números mayores que 20.")
            return False
    return True

def calcularPromedio(array):
    if not array:
        return 0
    return sum(array) / len(array)

leerNumerosHastaOcho(arrayNumeros,arrayNoEntraron)
promedio = calcularPromedio(arrayNoEntraron)
print(arrayNumeros)
print(arrayNoEntraron)
print(promedio)
