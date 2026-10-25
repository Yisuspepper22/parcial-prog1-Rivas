# Esta funcion es para calcular el promedio de las notas de los alumnos.
def calcular_promedio(nota_1, nota_2):
    """Calcula el promedio de dos notas."""
    promedio = (nota_1 + nota_2) / 2
    return promedio


# Esta funcion es para calcular el promedio general del curso.
def calcular_promedio_general(promedios):
    """Calcula el promedio general del curso."""
    acumulador = 0

    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]

    promedio_general = acumulador / len(promedios)

    return promedio_general


# Esta funcion es para buscar a el alumno con el mejor promedio.
def buscar_mejor_promedio(promedios):
    """Busca la posición del alumno con el mejor promedio."""
    mejor = promedios[0]
    posicion_mejor = 0

    for i in range(1, len(promedios)):
        if promedios[i] > mejor:
            mejor = promedios[i]
            posicion_mejor = i

    return posicion_mejor


# Esta funcion es para buscar a el alumno con el peor promedio.
def buscar_peor_promedio(promedios):
    """Busca la posición del alumno con el peor promedio."""
    peor = promedios[0]
    posicion_peor = 0

    for i in range(1, len(promedios)):
        if promedios[i] < peor:
            peor = promedios[i]
            posicion_peor = i

    return posicion_peor


# Esta funcion es para buscar que alumnos aprobaron o desaprobaron el curso.
def contar_condiciones(promedios):
    """Cuenta alumnos según su condición académica."""
    promocionan = 0
    aprueban = 0
    desaprueban = 0

    for i in range(len(promedios)):
        if promedios[i] >= 6:
            promocionan = promocionan + 1
        elif promedios[i] >= 4:
            aprueban = aprueban + 1
        else:
            desaprueban = desaprueban + 1

    return promocionan, aprueban, desaprueban


# Esta funcion es para ordenar los promedios.
def ordenar_por_promedio(promedios, nombres, notas_parcial_1, notas_parcial_2):
    """Ordena los alumnos de mayor a menor promedio."""

    for i in range(len(promedios) - 1):
        for j in range(len(promedios) - 1 - i):

            if promedios[j] < promedios[j + 1]:

                auxiliar = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = auxiliar

                auxiliar = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = auxiliar

                auxiliar = notas_parcial_1[j]
                notas_parcial_1[j] = notas_parcial_1[j + 1]
                notas_parcial_1[j + 1] = auxiliar

                auxiliar = notas_parcial_2[j]
                notas_parcial_2[j] = notas_parcial_2[j + 1]
                notas_parcial_2[j + 1] = auxiliar
                

# Funcion para contar vocales de los nombres de los alumnos.
def contar_vocales(nombre):
    """Cuenta la cantidad de vocales de un nombre."""

    vocales = 0

    for i in range(len(nombre)):
        letra = nombre[i]

        if (letra == "a" or letra == "e" or letra == "i"
                or letra == "o" or letra == "u"
                or letra == "A" or letra == "E" or letra == "I"
                or letra == "O" or letra == "U"):
            vocales = vocales + 1

    return vocales


#Funcion para realizar el juego con nombres de los alumnos.
def invertir_nombre(nombre):
    """Devuelve un nombre escrito al revés."""

    nombre_invertido = ""

    for i in range(len(nombre) - 1, -1, -1):
        nombre_invertido = nombre_invertido + nombre[i]

    return nombre_invertido


# Funcion para la busqueda de un nombre en la lista de alumnos.
def buscar_alumno(nombre_buscado, nombres):
    """Busca un alumno y devuelve su posición, o -1 si no existe."""

    posicion = -1

    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            posicion = i

    return posicion