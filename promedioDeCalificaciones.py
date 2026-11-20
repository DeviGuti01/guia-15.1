calificaciones = {}

cantidad = int(input("¿Cuántos estudiantes vas a ingresar?: "))

for i in range(cantidad):
    nombre = input("Ingresa el nombre del estudiante: ")
    nota = float(input("Ingresa la calificación: "))

    calificaciones[nombre] = nota

promedio = sum(calificaciones.values()) / len(calificaciones)

print("Calificaciones:", calificaciones)
print("Promedio general:", promedio)