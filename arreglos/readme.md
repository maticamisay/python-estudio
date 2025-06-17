# 🐍 Arreglos (Listas) en Python

## ✅ ¿Qué es un arreglo?

En Python, un arreglo se implementa comúnmente como una **lista**: una colección ordenada y mutable de elementos.

```python
numeros = [1, 2, 3, 4]
nombres = ["Ana", "Luis", "Pedro"]
````

## 🔧 Operaciones básicas

* **Acceder a elementos:**

  ```python
  nombres[0]  # "Ana"
  ```

* **Modificar elementos:**

  ```python
  nombres[1] = "Lucía"
  ```

* **Agregar elementos:**

  ```python
  nombres.append("Marta")
  ```

* **Insertar en una posición específica:**

  ```python
  nombres.insert(2, "Carlos")
  ```

* **Eliminar elementos:**

  ```python
  nombres.remove("Pedro")  # Por valor
  del nombres[0]           # Por índice
  ```

* **Recorrer con for:**

  ```python
  for nombre in nombres:
      print(nombre)
  ```

* **Slicing (rebanado):**

  ```python
  nombres[1:3]  # desde el índice 1 hasta el 2 (no incluye el 3)
  ```

## 🧠 Métodos útiles

```python
len(lista)           # Cantidad de elementos
lista.sort()         # Ordena (ascendente)
lista.reverse()      # Invierte el orden
lista.count(x)       # Cuenta cuántas veces aparece x
lista.index(x)       # Devuelve el índice de x
```

---

# 🧪 Ejercicios Prácticos

## 🟢 Nivel Básico

1. Crear una lista con 5 nombres y mostrar cada uno en una línea.
2. Agregar un nombre nuevo y mostrar la lista actualizada.
3. Eliminar el segundo nombre y mostrar la lista.
4. Mostrar la cantidad de elementos en la lista.
5. Ordenar la lista alfabéticamente.

## 🟡 Nivel Intermedio

6. Dada una lista de números, imprimir solo los pares.
7. Calcular la suma total de una lista de números.
8. Invertir una lista sin usar `.reverse()` ni slicing.
9. Contar cuántas veces aparece un valor dado (por input).
10. Reemplazar todas las apariciones de un valor por otro.

## 🔴 Nivel Avanzado

11. Combinar dos listas en una sola sin duplicados.
12. Eliminar los valores repetidos de una lista.
13. Hacer una función que reciba una lista y devuelva una nueva con solo los valores únicos.
14. Crear una matriz 3x3 con listas anidadas e imprimirla de forma estructurada.
15. Rotar una lista una posición a la derecha (ej: `[1, 2, 3]` → `[3, 1, 2]`).

---

> 💡 Consejo: intenta resolver sin usar librerías externas como NumPy, salvo que estés practicando específicamente eso.

