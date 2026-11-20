diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

invertido = {}

for clave, valor in diccionario.items():
    invertido[valor] = clave

print("Diccionario original:", diccionario)
print("Diccionario invertido:", invertido)