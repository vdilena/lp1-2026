# Alumno 1
alumnoUnoNombre = "Carolina Gomez"
alumnoUnoFechaNacimiento = "15/08/2000"
alumnoUnoNotaUltimoFinal = 8
alumnoUnoCantidadFinalesAprobados = 3
datosAlumnoUnoFecha = alumnoUnoFechaNacimiento.split("/")
# print(f"Dato de año: {datosFecha[2]}")
datoAlumnoUnoMenorOMayor = ""

if (2026 - int(datosAlumnoUnoFecha[2])) >= 18:
    datoAlumnoUnoMenorOMayor = " es mayor"
else:
    datoAlumnoUnoMenorOMayor = " es menor"

print(
    "Bienvenida "
    + alumnoUnoNombre
    + " que nació el "
    + alumnoUnoFechaNacimiento
    + " que se saco en el ultimo final "
    + str(alumnoUnoNotaUltimoFinal)
    + " y aprobo "
    + str(alumnoUnoCantidadFinalesAprobados)
    + " finales "
    + " y"
    + datoAlumnoUnoMenorOMayor
)


""" # Alumno 2
alumnoDosNombre = "Juan Perez"
alumnoDosFechaNacimiento = "02/03/1995"
alumnoDosNotaUltimoFinal = 5
alumnoDosCantidadFinalesAprobados = 1
print(
    f"Bienvenido {alumnoDosNombre} que nació el {alumnoDosFechaNacimiento} que se saco en el ultimo final {str(alumnoDosNotaUltimoFinal)} y aprobo {str(alumnoDosCantidadFinalesAprobados)} finales"
)

# Alumno 3
alumnoTresNombre = "Santiago Gimenez"
alumnoTresFechaNacimiento = "19/07/1988"
alumnoTresNotaUltimoFinal = 10
alumnoTresCantidadFinalesAprobados = 4
print(
    f"Bienvenido {alumnoTresNombre} que nació el {alumnoTresFechaNacimiento} que se saco en el ultimo final {str(alumnoTresNotaUltimoFinal)} y aprobo {str(alumnoTresCantidadFinalesAprobados)} finales"
)

# Alumno 4
alumnoCuatroNombre = "Julieta Salvatierra"
alumnoCuatroFechaNacimiento = "06/12/1999"
alumnoCuatroNotaUltimoFinal = 10
alumnoCuatroCantidadFinalesAprobados = 12
print(
    f"Bienvenido {alumnoCuatroNombre} que nació el {alumnoCuatroFechaNacimiento} que se saco en el ultimo final {str(alumnoCuatroNotaUltimoFinal)} y aprobo {str(alumnoCuatroCantidadFinalesAprobados)} finales"
) """
