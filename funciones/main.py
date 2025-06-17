# 1. Crear una función que imprima "Hola Mundo".
def hola_mundo():
    print("Hola Mundo")

# 2. Crear una función que reciba un nombre y salude.
def saludar(nombre):
    print(f"Hola {nombre}") #usamos print(f) para que el nombre se imprima en la consola

# 3. Crear una función que reciba dos números y retorne su suma.
def sumar(a,b):
    return a + b

print(sumar(1,2))

# 4. Crear una función que reciba un número y retorne su cuadrado.
def cuadrado(a):
    return a*a

print(cuadrado(6))

# 5. Crear una función que diga si un número es par o impar.
def isPar(num):
    return num%2==0

print(isPar(2))
print(isPar(7))
print(isPar(8))

# 6. Crear una función que reciba una lista de números y devuelva la suma total.
listaNum = [1,2,3,4,5]
def sumaLista (array):
    suma = 0
    for num in array:
        suma += num
    return suma

print(sumaLista(listaNum))

# 7. Crear una función que reciba una cadena y cuente cuántas vocales tiene.
def contarVocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

print(contarVocales("Hola Mundo"))

# 8. Crear una función que reciba una lista y devuelva una nueva con solo los valores únicos.
def listaUnica(lista):
    return list(set(lista))
print(listaUnica([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]))


# 9. Crear una función que reciba un número entero y retorne True si es primo.


# 10. Crear una función que convierta grados Celsius a Fahrenheit.
