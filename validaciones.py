# Esta función es para validar la cantidad de alumnos.
def validar_cantidad_de_alumnos():
    """Solicita una cantidad de alumnos entre 1 y 30."""

    cantidad = int(input("Ingrese la cantidad de alumnos: "))

    while cantidad < 1 or cantidad > 30:
        print("Cantidad invalida. Ingrese un numero entre 1 y 30.")
        cantidad = int(input("Ingrese la cantidad de alumnos: "))
    return cantidad


# Esta funcion valida los nombres de los alumnos.
def validar_nombre():
    """Solicita un nombre válido."""

    nombre = input("Ingrese el nombre del alumno: ")

    while True:
        nombre_valido = True

        if len(nombre) < 5:
            nombre_valido = False

        for i in range(len(nombre)):
            caracter = nombre[i]

            minuscula = "a" <= caracter <= "z"
            mayuscula = "A" <= caracter <= "Z"
            espacio = caracter == " "

            if not (minuscula or mayuscula or espacio):
                nombre_valido = False

        if nombre_valido:
            return nombre

        print("Nombre invalido. Debe tener al menos 5 caracteres "
            "y contener solamente letras y espacios.")

        nombre = input("Ingrese el nombre del alumno: ")


# Esta funcion valida las notas de los alumnos.
def validar_nota(parcial):
    """Solicita una nota entre 0 y 10."""

    nota = input(f"Ingrese la nota del {parcial}: ")
    nota_valida = False

    while not nota_valida:

        if nota == "10" or (len(nota) == 1 and "0" <= nota <= "9"):
            nota_valida = True
        else:
            print("Nota invalida. Ingrese un numero entero entre 0 y 10.")
            nota = input(f"Ingrese la nota del {parcial}: ")
    return int(nota)