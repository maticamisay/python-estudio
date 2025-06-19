#  Ingresar números hasta cargar un arreglo de 10 elementos de la siguiente manera:
# 5 positivos y 5 negativos en ese orden. Calcular y mostrar:
# a. El promedio de los números negativos.
# b. Ordenar el arreglo de menor a mayor.
# c. Generar otro arreglo con los múltiplos de 4. Si no los hubiese mostrar cartel
# aclaratorio.
# d. Mostrar cuántos pares y cuántos múltiplos de 3 hay en este último arreglo.

def cargar_arreglo():
    positivos = []
    negativos = []
    for i in range(5):
        n = int(input("Ingrese un numero positivo: "))
        while n<0:
            print("el numero debe ser estrictamente positivo, intente nuevamente")
            n = int(input("Ingrese un numero positivo: "))
        print(i,n)
        positivos.append(n)
    for i in range(5):
        n = int(input("Ingrese un numero negativo: "))
        while n>0:
            print("el numero debe ser estrictamente negativo, intente nuevamente")
            n = int(input("Ingrese un numero negativo: "))
        negativos.append(n)
    return positivos+negativos

def promNegativos(arr):
    return sum(arr)/len(arr)

def hayMultiplos(arr):
    newArray = []
    for i in range(len(arr)):
        if(arr[i]%4==0):
            newArray.append(arr[i])
    
    if not newArray:
        return print("no hay multiplos de 4")
    
    return print(f"Multiplos de 4: {newArray}")

def ordenar(arr):
    arr.sort()

array = cargar_arreglo()
print(array)
print(f"promedio {promNegativos(array)}")
hayMultiplos(array)
ordenar(array)
print(f"array ordenado {array}")

