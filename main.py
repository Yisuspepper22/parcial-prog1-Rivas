# Importamos las funciones de validaciones y procesamientos.
from validaciones import (validar_cantidad_de_alumnos,validar_nombre,validar_nota)
from procesamientos import (calcular_promedio,calcular_promedio_general,buscar_mejor_promedio, 
buscar_peor_promedio,contar_condiciones,ordenar_por_promedio,contar_vocales,invertir_nombre, buscar_alumno)


# Listas donde guardamos los datos de los alumnos.
nombres = []
notas_parcial_1 = []
notas_parcial_2 = []
promedios = []


# Menú principal.
while True:
    print("========== NOTAFÁCIL ==========") 
    print("1. Cargar alumno")
    print("2. Mostrar listado")
    print("3. Mostrar estadísticas")
    print("4. Ver ranking ordenado")
    print("5. Buscar alumno")
    print("6. Jugar con un nombre")
    print("0. Salir")

    opcion = input("Elegí una opción: ")

    match opcion:

        # OPCIÓN 1: Cargar un alumno.
        case "1":
            print("--- Cargar alumnos ---")

            cantidad = validar_cantidad_de_alumnos()

            for i in range(cantidad):
                print("\nAlumno número", i + 1)

                nombre = validar_nombre()
                nota_1 = validar_nota("primer parcial")
                nota_2 = validar_nota("segundo parcial")

                promedio = calcular_promedio(nota_1, nota_2)

                nombres = nombres + [nombre]
                notas_parcial_1 = notas_parcial_1 + [nota_1]
                notas_parcial_2 = notas_parcial_2 + [nota_2]
                promedios = promedios + [promedio]

                print("Alumno cargado correctamente.")
                print("Promedio:", promedio)

            print("Carga de alumnos finalizada.")


        # OPCIÓN 2: Mostrar el listado.
        case "2":
            print("--- Listado de alumnos ---")

            if len(nombres) == 0:
                print("Todavía no hay alumnos cargados.")
            else:
                for i in range(len(nombres)):
                    print(nombres[i],"- Nota 1:", notas_parcial_1[i],
                        "- Nota 2:", notas_parcial_2[i],
                        "- Promedio:", promedios[i])

        # OPCIÓN 3: Mostrar estadísticas.
        case "3":
            print("--- Estadísticas del curso ---")

            if len(nombres) == 0:
                print("Primero tenés que cargar un alumno.")
            else:
                promedio_general = calcular_promedio_general(promedios)
                posicion_mejor = buscar_mejor_promedio(promedios)
                posicion_peor = buscar_peor_promedio(promedios)
                promocionan, aprueban, desaprueban = (contar_condiciones(promedios))

                print("Promedio general del curso:",promedio_general)

                print("Mejor alumno:")
                print("Nombre:", nombres[posicion_mejor])
                print("Promedio:", promedios[posicion_mejor])

                print("Peor alumno:")
                print("Nombre:", nombres[posicion_peor])
                print("Promedio:", promedios[posicion_peor])

                print("Condición académica:")
                print("Alumnos que promocionan:", promocionan)
                print("Alumnos que aprueban:", aprueban)
                print("Alumnos que desaprueban:", desaprueban)

        # OPCIÓN 4: Ver el ranking ordenado.
        case "4":
            print("--- Ranking por promedio ---")

            if len(nombres) == 0:
                print("Primero tenés que cargar un alumno.")
            else:
                ordenar_por_promedio(promedios,nombres,notas_parcial_1,notas_parcial_2)

                for i in range(len(nombres)):
                    print(i + 1, "-",nombres[i],
                        "- Nota 1:", notas_parcial_1[i],
                        "- Nota 2:", notas_parcial_2[i],
                        "- Promedio:", promedios[i])

        # OPCIÓN 5: Buscar un alumno.
        case "5":
            print("--- Buscar alumno ---")

            if len(nombres) == 0:
                print("Primero tenés que cargar un alumno.")
            else:
                nombre_buscado = validar_nombre()

                posicion = buscar_alumno(nombre_buscado,nombres)

                if posicion != -1:
                    print("Alumno encontrado:", nombres[posicion])
                    print("Nota del primer parcial:",notas_parcial_1[posicion])
                    print("Nota del segundo parcial:", notas_parcial_2[posicion])
                    print("Promedio:", promedios[posicion])
                else:
                    print("No se encontró ese alumno.")

        # OPCIÓN 6: Jugar con un nombre.
        case "6":
            print("--- Jugar con un nombre ---")

            nombre = validar_nombre()

            cantidad_vocales = contar_vocales(nombre)
            nombre_invertido = invertir_nombre(nombre)

            print("Cantidad de vocales:", cantidad_vocales)
            print("Nombre invertido:", nombre_invertido)

        # OPCIÓN 0: Salir.
        case "0":
            print("¡Gracias por usar NotaFácil!")
            break

        # Cualquier otra opción.
        case _:
            print("Opción inválida. Elegí una opción del menú.")