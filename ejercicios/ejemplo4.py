CANTIDAD_TOTAL_FINALES = 40


def alumnoCreado(nombre, fechaNac, notaFinal, cantFinalesAprobados):
    nuevoAlumno = {
        "nombre": nombre,
        "fechaNacimiento": fechaNac,
        "notaFinal": notaFinal,
        "cantFinalesAprobados": cantFinalesAprobados,
    }

    return nuevoAlumno


def alumnoMayorOMenor(fechaNac):
    datosAlumnoFecha = fechaNac.split("/")
    resultado = ""
    if (2026 - int(datosAlumnoFecha[2])) >= 18:
        resultado = " es mayor"
    else:
        resultado = " es menor"

    return resultado


def mostrarAlumno(alumno):
    print(
        "Bienvenida "
        + alumno["nombre"]
        + " que nació el "
        + alumno.get("fechaNacimiento")
        + " que se saco en el ultimo final "
        + str(alumno["notaFinal"])
        + " y aprobo "
        + str(alumno.get("cantFinalesAprobados"))
        + " finales "
        + " y"
        + alumnoMayorOMenor(alumno.get("fechaNacimiento"))
        + " y le quedan "
        + str(CANTIDAD_TOTAL_FINALES - alumno.get("cantFinalesAprobados"))
        + " finales para recibirse"
    )


# Alumno 1
alumnoUno = alumnoCreado("Carolina Gomez", "15/08/2000", 8, 3)
mostrarAlumno(alumnoUno)

# Alumno 2
alumnoDos = alumnoCreado("Juan Perez", "02/03/2012", 5, 1)
mostrarAlumno(alumnoDos)

# Alumno 3
alumnoTres = alumnoCreado("Santiago Gimenez", "19/07/1988", 10, 4)
mostrarAlumno(alumnoTres)

# Alumno 4
alumnoCuatro = alumnoCreado("Julieta Salvatierra", "06/12/1999", 10, 12)
mostrarAlumno(alumnoCuatro)
