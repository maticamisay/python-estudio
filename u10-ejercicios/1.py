# 1. Diseñar con funciones el siguiente programa en Python:
# a. Se carga A con 10 números pares y B con 10 números múltiplos de 5.
# b. Cargar el arreglo C con la suma de cada elemento de A con cada elemento de B.
# c. Cargar el arreglo D con los todos los elementos de A y a continuación todos los elementos de B.
# d. Invertir el arreglo A sobre sí mismo.
# e. Buscar la posición del máximo de B. Mostrar la posición del máximo y el valor del máximo. Poner en cero los valores a la derecha del máximo.
# f. Encontrar el promedio de C. Contar cuántos valores hay en C por encima de ese promedio

# a.
A=[2,4,6,8,10,12,14,16,18,20]
B=[5,10,15,20,25,30,35,40,45,50]

# b.
C=[]
for i in range(len(A)):
    C.append(A[i]+B[i])
print(C)

# c.
D=[]
D.extend(A)
D.extend(B)
print(D)

# d.
A.reverse()
print(A)

# e.
B_new=[8,6,12,2,10,14,4,40,18,20]
def posicion_maximo(B):
    max=B[0]
    for i in range(len(B)):
        if B[i]>max:
            max=B[i]
            posicion=i
    for i in range(posicion+1, len(B)):
        B[i]=0
    return posicion, max

posicion, max=posicion_maximo(B_new)
print(posicion, max, B_new)

# f.
promedio=sum(C)/len(C)
print(promedio)

def promedio_superior(C, promedio):
    contador=0
    for i in range(len(C)):
        if C[i]>promedio:
            contador+=1
    return contador

contador=promedio_superior(C, promedio)
print(contador)