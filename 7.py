# Modifique el ejercicio anterior, solo que ahora se desea que el cálculo se haga para cada uno de los
# grupos de fundamentos de programación. El programa recibe como entrada la cantidad de grupos y
# para grupo, debe realizar lo indicado en el ejercicio anterior
amount_groups = int(input("Cuantos grupos hay? "))
total_aproved_students = 0
total_extension_students = 0
total_fail_students = 0

for groups in range(0,amount_groups):
    aproved_students = 0
    extension_students = 0
    fail_students = 0
    amount_students = int(input(f"Cuantos estudiantes fueron evaluados en el grupo #{groups + 1}? "))
    amount_exams = int(input("Cuantos examenes realizaron? "))
    for student in range(0,amount_students):
        all_exams = 0
        for i in range(0,amount_exams):
            all_exams += int(input(f"Cual fue la nota del examen {i + 1} para el estudiante {student + 1} "))
        average = all_exams / amount_exams

        if average >= 70:
            total_aproved_students += 1
            aproved_students += 1
        elif average < 70 and average >= 60:
            total_extension_students += 1
            extension_students += 1
        elif average < 60:
            total_fail_students += 1
            fail_students += 1
        else:
            print("Invalid input")
    print(f"Resultados del grupo {groups + 1}:")
    print(f"Estudinates aprobados: {aproved_students}")
    print(f"Estudinates con ampliacion: {extension_students}")
    print(f"Estudinates reprobados {fail_students}")

print("Resultados totales:")
print(f"Estudinates aprobados: {total_aproved_students}")
print(f"Estudinates con ampliacion: {total_extension_students}")
print(f"Estudinates reprobados {total_fail_students}")