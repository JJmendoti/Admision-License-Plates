#Una institución educativa se encuentra en proceso de finalizar semestre y en proceso de admisión para el próximo semestre. La institución requiere un software que le permita solucionar estas dos problemáticas con las siguientes restricciones.
#Para finalización de semestre:
#Se desean subir las notas de los alumnos al sistema de los programas creados, para ello, se le pide al docente el número de alumnos, nombre de cada alumno, programa académico, si es hombre, mujer, no binario, además, las 5 notas obtenidas durante el curso. El software calcula el promedio de las 5 notas. Al finalizar la ejecución debe mostrar cuántos hombres, mujeres y no bonarios hay en cada programa académico, el promedio de notas por cada programa y el listado de alumnos con el respectivo promedio de cada uno.
#Para el proceso de admisión

#La institución requiere que se le muestre cuántos estudiantes en total se matricularon y el promedio de edad de los matriculados, además, requiere saber cuántos hombres y mujeres se matricularon.
#El proceso de admisión termina hasta que el usuario decida que ya no se van a matricular más personas.

# "Requerimientos Adicionales"
#el usuario puede ingresar los programas académicos que desee y en base a esto escogera a que programa pertenece
#Debe contar cuantos estudiantes hay por programa académico registrado debe llevar las validaciones de

#"validaciones"

#ejemplo para el sexo: el user puede ingresar "m" "h" "nb"
#si no se ingresas los datos validos el programa no dede funcionar ¿, obligando al usr a ingresar los datos correctos ; si el dato no es valido se queda en ciclo infinito las validaciones aplican para todos los datos que se van a ingresar.

# aplica también si el usuario ingresa un programa académico que no se encuentra en el arreglo.
# ejemplo: si el elige un programa y no esta el programa se queda hasta que ingrese un programa académico valido del arreglo.
#Si el sexo ingresado no es valido se queda en ciclo infinito hasta que ingrese la letra que es.

#El software debe ser dinamico
#al final debe mostrar cuantos estudiantes hay por programa académico.

numAlumnos = 0
students = []
countStudents = 0
averageAge = 0
academicProgram = []
numacademicProgram = 0
flag_ciclo_program = True
array_students = []


print("Bienvenido al programa de matriculas y admisiones uvagancia")
print("Para continuar por favor crea los programas Académicos ")


while flag_ciclo_program:
    print("Ingrese el nombre del nuevo programa. \n")
    new_name_program = input("Nombre: ")
    academicProgram.append(new_name_program)
    print(f"Se ha creado el nuevo programa {new_name_program} ")
    print("Los programas creados hasta el momento son: " +
          str(academicProgram)+"\n\n")
    print("Desea ingresar otro programa?")
    print("Ingrese el número 1 para crear otro programa académico")
    print("Ingrese 0 o cualquier tecla para dejar crear programas\n\n")
    try:
        answer = int(input("Ingrese 1 ó 0:  "))
        valid_number_of_students = True
    except:
        valid_number_of_students = False
    while(not valid_number_of_students or answer<0 or answer>1):
        try:
            print('Opción no permitida. Intente de nuevo')
            print("Ingrese el número 1 para crear otro programa académico")
            print("Ingrese 0 o cualquier tecla para dejar crear programas\n\n")
            answer = int(input("Ingrese 1 ó 0:  "))
            valid_number_of_students = True
        except:
            print('Opción no permitida. Intente de nuevo')
            valid_number_of_students = False
    if answer != 1:
        flag_ciclo_program = False

print("------------------------------------------------------------------------------------")

def averageStudent():
    average = 0
    for j in range(1, 6):
        try:
            average = average + float(input(f"Ingrese nota {j}: "))
        except:
            print('\nNota inválida, vuelva a ingresar las notas para este alumno.\n')
            return False
    average = average / 5
    return average

menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri) \n")
while(menu != 'admi' and menu != 'matri'):
    print('Opción inválida. intente de nuevo')
    menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri) \n")

if menu == "admi":
    try:
        numAlumnos = int(input("Ingrese número de alumnos: \n"))
        valid_number_of_students = True
    except:
        valid_number_of_students=False

    while (not valid_number_of_students or numAlumnos<1):
        try:
            print('Error. Asegúrese de ingresar un valor numérico y que este sea mayor que "cero". Intente de nuevo')
            numAlumnos = int(input("Ingrese número de alumnos: \n"))
            valid_number_of_students = True
        except:
            valid_number_of_students=False


    for i in range(numAlumnos):
        name = input("Ingrese nombre del alumno: \n")
        print("Elija un programa ")
        program_counter = 0
        for program in academicProgram:
            print(str(program_counter)+". "+str(program))
            program_counter += 1
        try:
            selected_program = int(input("Programa: \n"))
        except:
            print('El valor ingresdo para el programa debe ser numérico. intente de nuevo\n')
            selected_program=-1
        while((selected_program > (len(academicProgram)-1)) or (selected_program < 0)):
            print('\nNo hemos podido reconocer el programa, intenta de nuevo.\n')
            program_counter = 0
            for program in academicProgram:
                print(str(program_counter)+". "+str(program))
                program_counter += 1
            try:
                selected_program = int(input("Programa: \n"))
            except:
                print(
                    'El valor ingresdo para el programa debe ser numérico. intente de nuevo\n')
                selected_program = -1

        sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario) \n")
        while(sex != 'm' and sex != 'h' and sex != 'nb'):
            print(f"Su eleccion de sexo '{sex}', no se reconoce. Intente de nuevo.\n")
            sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario) \n")
        average = averageStudent()
        while(not average):
            average = averageStudent()
        array_students.append(
            {"name": name, "program": selected_program, "sex": sex, "average": average})

    array_average_programs = []
    print('\n\n---------------------------------------------------------------------------')
    print('RESULTADOS DE ESTUDIANTES')
    print('---------------------------------------------------------------------------\n')

    for k in range(0, len(academicProgram)):
        acumulador_average_program = 0
        conunter_average_program = 0
        counter_women = 0
        counter_men = 0
        counter_no_binary = 0
        for student in array_students:

            if(int(k) == int(student['program'])):
                acumulador_average_program += float(student['average'])
                conunter_average_program += 1
                if(student['sex'] == 'm'):
                    counter_women += 1
                elif (student['sex'] == 'h'):
                    counter_men += 1
                else:
                    counter_no_binary += 1
        if conunter_average_program == 0:
            print(f"El programa {academicProgram[k]} no registra alumnos. \n")
        else:
            print(f"El promedio del programa {academicProgram[k]} es: {str((float(acumulador_average_program)/conunter_average_program))} ")
            print(f"La cantidad de mujeres en el programa {academicProgram[k]} es: {str(counter_women)}")
            print(f"La cantidad de hombres en el programa {academicProgram[k]} es: {str(counter_men)}")
            print(f"La cantidad de no binarios en el programa {academicProgram[k]} es: {str(counter_no_binary)}\n")
            print('---------------------------------------------------------------------------\n')

    print("\n\nLos alumnos son:\n ")
    for student in array_students:
        print(
            f"{student['name']}\t\tprograma: {academicProgram[int(student['program'])]}\t\tpromedio {student['average']} ")
        print('---------------------------------------------------------------------------\n')
else:
    countWomen = 0
    countMen = 0
    countNb = 0
    while True:
        sexValidate = True
        try:
            averageAge += int(input("Ingrese la edad: \n"))
            ageStudents = True
        except:
            ageStudents = False
        while(not ageStudents or averageAge<1):
            try:
                print('Error. Por favor Asegúrese de ingresar un valor numérico y que este sea mayor que "cero". Intente de nuevo')
                averageAge += int(input("Ingrese la edad: \n"))
                ageStudents = True
            except:
                ageStudents = False
        while sexValidate:  
            sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario) \n")
            if sex != 'm' and sex != 'h' and sex != 'nb':
                print(f"no hemos reconocido su eleccion de sexo '{sex}'. Intente de nuevo.\n")
            if sex == "m":
                countWomen += 1
                sexValidate = False
            elif sex == "h":
                countMen += 1
                sexValidate = False
            elif sex == "nb":
                countNb += 1
                sexValidate = False
        stopAdmission = input("\n si desea parar de matricular ingrese 0, de lo contrario cualquier tecla para continuar \n")
        countStudents += 1
        if stopAdmission == "0":
            break

    averageAge = averageAge/countStudents
    print('\n---------------------------------------------------------------------------')
    print('RESULTADOS DE MATRICULADOS')
    print('---------------------------------------------------------------------------\n')
    print(f"Número de estudiantes matriculados: {countStudents}")
    print(f"Promedio de edad de matriculados: {averageAge}")
    print(f"Número de mujeres matriculadas: {countWomen}")
    print(f"Número de hombres matriculadas: {countMen}")
    print(f"Número de no binarios matriculados: {countNb}")
    print('---------------------------------------------------------------------------\n')
