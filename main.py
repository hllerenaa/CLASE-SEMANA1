nombre = 'HECTOR'
apellido = "LLERENA"
materia = """PROGRAMACION PYTHON"""
edad = 31
listas = [1, 2, 3, 4, 5]
cerrar = True
abrir = False


print(materia)
print(f"NOMBRE: {nombre} {apellido}")

if edad == 30:
    print("TIENES 30 AÑOS")
elif edad > 30:
    print("TIENES MAS DE 30 AÑOS")
elif edad < 30:
    print(f"ERES MENOR: {edad}")

suma = 0
suma_2 = 0
for i in listas:
    suma += 1
    suma_2 += i

print(f"SUMA: {suma}")
print(f"SUMA: {suma_2}")