n = int(input("Ingresa el tamaño de la matriz: "))

matriz = []

for fila in range(n):
    fila_actual = []

    for columna in range(n):
        if fila == columna:
            fila_actual.append(1)
        else:
            fila_actual.append(0)

    matriz.append(fila_actual)

print("Matriz identidad:")

for fila in matriz:
    print(fila)