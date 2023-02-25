# Haga un programa que dado un número entero N, imprima todos los números que son múltiplos entre
# 1 y N. Ejemplo: si N = 10, el programa imprime lo siguiente:
# Los múltiplos de 10, entre 1 y 10 son:
# 1
# 2
# 5
# 10

N = 10
i = 1
print(f"Los múltiplos de {N}, entre 1 y {N} son:")
while N >= i:
    if N % i == 0:
        print(i)
    i += 1
