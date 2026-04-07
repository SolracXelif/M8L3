import sys
# Este programa es un sistema de gestión de notas para estudiantes. Permite al usuario ingresar el nombre de un estudiante y muestra su estado de aprobación basado en sus notas y asistencia.
# sugiero cambiar las variables a tener nombres mas descriptivos, como "estudiantes", "notas" y "asistencia" para que sea mas facil de entender el codigo.
personas = ["Juan", "Maria", "Pedro"]
notas = [3.5, 4.2, 2.8]
asistencia = [True, True, False] 
# La función "logica" determina si un estudiante ha aprobado o no basado en su nota y asistencia. Si la nota es mayor o igual a 3.0 y la asistencia es True, el estudiante aprueba. Si la nota es mayor o igual a 3.0 pero la asistencia es False, el estudiante falla por faltas. Si la nota es menor a 3.0, el estudiante reproba.
# Sugiero simplificar la lógica de esta función para que sea más fácil de entender, eliminando la necesidad de anidar condicionales.
def logica(p):
    # Lógica de "aprobación" innecesariamente compleja
    if notas[p] >= 3.0:
        if asistencia[p] == True:
            return "PASO"
        else:
            return "FALLO POR FALTAS"
    else:
        return "REPROBADO"
# cambiar el nombre de la funcion a algo que haga mas sentido que z(), como mostrar. Tambien agregar un mensaje para que el usuario sepa que debe ingresar el nombre del estudiante o "fin" para salir. Y agregar un mensaje para que el usuario sepa que se encontró el estudiante y mostrar su resultado, nota y asistencia. Si el nombre no existe, el programa simplemente no hace nada.
def mostrar():
    # Función para buscar y mostrar
    while True:
        # Agregar un mensaje para que el usuario sepa que debe ingresar el nombre del estudiante o "fin" para salir.
        nombre = input("Ingrese el nombre del estudiante para ver sus notas o escribe fin para acabar: ")
        if nombre == "fin":
            break
        for i in range(len(personas)):
            if personas[i] == nombre:
                resultado = logica(i)
                # Agregar un mensaje para que el usuario sepa que se encontró el estudiante y mostrar su resultado, nota y asistencia.
                print(personas[i] + " - " + resultado + " - Nota: " + str(notas[i]) + " - Asistencia: " + str(asistencia[i]))
        # Si el nombre no existe, el programa simplemente no hace nada. Hay que agregar un mensaje para que el usuario sepa que el estudiante no fue encontrado.
        if nombre not in personas:
            print("Estudiante no encontrado.")
mostrar()