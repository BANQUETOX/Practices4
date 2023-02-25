# Modifique el ejercicio anterior de la siguiente manera: el programa debe calcular ahora la cantidad de
# estudiantes que aprobó el curso, la cantidad de estudiantes que reprobó y la cantidad que fue a
# ampliación. Para esto el programa ahora, adicionalmente recibe el número de estudiantes del curso.
# No olvide tener en cuenta lo mencionado en el ejercicio anterior.
amount_students = int(input("Cuantos estudiantes fueron evaluados? "))
amount_exams = int(input("Cuantos examenes realizaron? "))
aproved_students = 0
extension_students = 0
fail_students = 0


for student in range(0,amount_students):
    all_exams = 0
    for i in range(0,amount_exams):
        all_exams += int(input(f"Cual fue la nota del examen {i + 1} para el estudiante {student + 1} "))
    average = all_exams / amount_exams

    if average >= 70:
        aproved_students += 1
    elif average < 70 and average >= 60:
        extension_students += 1
    elif average < 60:
        fail_students += 1
    else:
        print("Invalid input")
    
print(f"Estudinates aprovados: {aproved_students}")
print(f"Estudinates con ampliacion: {extension_students}")
print(f"Estudinates reprobados {fail_students}")