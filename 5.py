# Haga un programa que reciba como entrada la cantidad de exámenes realizados por un estudiante en
# un curso, y debe calcular la nota del curso que se obtiene del promedio de todos los exámenes. El
# programa deberá determinar además, si el estudiante aprobó, debe ir a ampliación o reprobó el curso.
# Un estudiante aprueba el curso si su nota es mayor o igual a 70, debe hacer ampliación si su nota es
# inferior a 70 pero superior o igual a 60, o reprueba el curso si la nota es menor que 60.

amount_exams = int(input("Cuantos examenes realizo? "))
all_exams = 0
for i in range(0,amount_exams):
    all_exams += int(input(f"Cual fue la nota del examen {i + 1} "))
average = all_exams / amount_exams

if average >= 70:
    print("Aprobo el curso")
elif average < 70 and average >= 60:
    print("Debe ir a ampliacion")
elif average < 60:
    print("Reprobo el curso")
else:
    print("Invalid input")