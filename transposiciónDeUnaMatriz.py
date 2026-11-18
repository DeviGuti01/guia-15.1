filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

matriz = []

for i in range(filas):
    fila = []

    for j in range(columnas):
        numero = int(input(f"Ingresa el elemento [{i}][{j}]: "))
        fila.append(numero)

    matriz.append(fila)

transpuesta = []

for j in range(columnas):
    fila = []

    for i in range(filas):
        fila.append(matriz[i][j])

    transpuesta.append(fila)

print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)