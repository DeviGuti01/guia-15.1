numeros = input("Ingresa los números separados por espacios: ")

lista = [int(numero) for numero in numeros.split()]

promedio = sum(lista) / len(lista)

mayores = [numero for numero in lista if numero > promedio]

print("Promedio:", promedio)
print("Mayores que el promedio:", sorted(mayores))