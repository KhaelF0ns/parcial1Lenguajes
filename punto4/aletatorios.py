import random

# Número de números a generar
num_count = 1000
# Rango de los números
min_val = 1
max_val = 1000

# Generar números aleatorios
numeros = [random.randint(min_val, max_val) for _ in range(num_count)]

# Guardar los números en un archivo
with open('numeros.txt', 'w') as file:
    for num in numeros:
        file.write(f"{num} \n")
