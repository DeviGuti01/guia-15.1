lista_a = input("Ingresa los números de la lista A: ")
lista_b = input("Ingresa los números de la lista B: ")

A = [int(numero) for numero in lista_a.split()]
B = [int(numero) for numero in lista_b.split()]

if len(A) == len(B):
    producto = sum(A[i] * B[i] for i in range(len(A)))
    print("Producto escalar =", producto)
else:
    print("Las listas deben tener el mismo tamaño")