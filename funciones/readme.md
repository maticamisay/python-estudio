# 🧠 Funciones en Python

## ✅ ¿Qué es una función?

Una función es un bloque reutilizable de código que se define una vez y se puede ejecutar varias veces.

```python
def saludar():
    print("Hola!")
```

## 🎯 ¿Por qué usar funciones?

* Evitan la repetición de código.
* Hacen el código más legible y modular.
* Permiten dividir problemas complejos en partes pequeñas.

## 🧱 Sintaxis básica

```python
def nombre_funcion(parámetros):
    # Cuerpo de la función
    return resultado
```

### Ejemplo:

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)  # resultado = 8
```

## 🧰 Tipos de parámetros

```python
# Parámetros por defecto
def saludar(nombre="Usuario"):
    print(f"Hola, {nombre}")

# Argumentos por nombre
saludar(nombre="Ana")
```

## 🔁 Funciones sin return vs con return

* `print()` solo muestra algo en pantalla.
* `return` devuelve un valor al código que llama a la función.

```python
def cuadrado(n):
    return n * n

x = cuadrado(4)  # x = 16
```

## 📌 Funciones Lambda

Funciones anónimas, útiles para operaciones simples.

```python
f = lambda x: x * 2
print(f(5))  # 10
```

---

# 🧪 Ejercicios Prácticos

## 🟢 Nivel Básico

1. Crear una función que imprima "Hola Mundo".
2. Crear una función que reciba un nombre y salude.
3. Crear una función que reciba dos números y retorne su suma.
4. Crear una función que reciba un número y retorne su cuadrado.
5. Crear una función que diga si un número es par o impar.

## 🟡 Nivel Intermedio

6. Crear una función que reciba una lista de números y devuelva la suma total.
7. Crear una función que reciba una cadena y cuente cuántas vocales tiene.
8. Crear una función que reciba una lista y devuelva una nueva con solo los valores únicos.
9. Crear una función que reciba un número entero y retorne True si es primo.
10. Crear una función que convierta grados Celsius a Fahrenheit.

## 🔴 Nivel Avanzado

11. Crear una función que reciba una función como parámetro y la aplique a una lista.
12. Crear una función que reciba cualquier cantidad de argumentos y devuelva la suma.
13. Crear una función que genere otra función (closures).
14. Crear una función recursiva que calcule el factorial de un número.
15. Crear un decorador que mida cuánto tarda en ejecutarse una función.

