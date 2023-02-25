# Haga un programa que imprima todos los números pares desde 1 hasta N, donde N es un número
# entero positivo. Ejemplo: si N=10, el programa imprime lo siguiente:

# Los números pares entre 1 y 10 son:
# 2
# 4
# 6
# 8
# 10

N = 10
number = 0
print(f"Los numero pares entre 1 y {N}")
while number <= N:
    if number % 2 == 0:
        print(number)
    number += 1