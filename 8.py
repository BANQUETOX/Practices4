# En la isla del Edén vive una gran cantidad de hormigas que se reproducen a una tasa del 40%
# mensual; en la isla existe además un oso hormiguero que se come 7000 hormigas al final de cada mes
# (o todas las hormigas que haya si la población de hormigas en ese momento es inferior a 7000).
# Cuando la población de hormigas de la isla sobrepasa el máximo de 28000, comienza a haber
# problemas de alimentación lo que hace que se reduzca la tasa de crecimiento al 31% mensual. El
# muestreo de la población se hace mensualmente, al final de cada mes. Haga un programa que reciba
# como entrada el número de hormigas que hay en un momento dado en la isla y un número entero X, y
# calcule la población de hormigas después de esos X meses.

months = int(input("Cuantos meses desea calcular? "))
amount_ants = int(input("Cuantas hormigas hay en la isla? "))
while months > 0:
    if amount_ants < 7000:
        amount_ants = 0
        break
    elif amount_ants > 28000:
        amount_ants += (amount_ants * 0.31)
    else:
        amount_ants += (amount_ants * 0.4)
    amount_ants -= 7000
    months -= 1

print(f"Habran {amount_ants.__round__()} hormigas en la isla")