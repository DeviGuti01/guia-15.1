A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

resultado = []

for i in range(len(A)):
    fila = []

    for j in range(len(A[i])):
        suma = A[i][j] + B[i][j]
        fila.append(suma)

    resultado.append(fila)

print("Resultado de la suma:")

for fila in resultado:
    print(fila)