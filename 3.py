# Se quiere calcular el factorial de un número entero N, que se define de la siguiente manera:
# n ! = 1 * 2 * 3* 4 * 5 … * n. n ! : se lee n factorial.
# • Ejemplo: si N = 5, se calcula: 5 ! = 1 * 2 * 3 * 4 * 5 = 120, el programa imprime:
# El factorial de 5 es: 120

N = 5
i = 0
result = 0
while N >= i :
    result += N * (N - 1)
    i += 1

print(f"El factorial de {N} es: {result}")