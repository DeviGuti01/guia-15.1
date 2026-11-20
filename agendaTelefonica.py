agenda = {}

while True:
    nombre = input("Ingresa el nombre (o escribe fin): ")

    if nombre.lower() == "fin":
        break

    telefono = input("Ingresa el teléfono: ")

    agenda[nombre] = telefono

print("Agenda telefónica:", agenda)