class Ciudadano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad
    
    def validar_edad(edad):
        return isinstance(edad, int) and edad >= 0


class Medico(Ciudadano):
    def __init__(self, nombre, edad, especialidad, hospital):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.hospital = hospital

    def diagnosticar(self, enfermedad):
        return f"El médico {self.nombre} ha diagnosticado {enfermedad}"

    def recetar_medicamento(self, medicamento):
        print(f"El médico {self.nombre} ha recetado el medicamento {medicamento}")


class Profesor(Ciudadano):
    def __init__(self, nombre, edad, asignatura, colegio):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
        self.colegio = colegio

    def enseñar(self, tema):
        return f"El profesor {self.nombre} está enseñando {tema}"

    def asignar_tarea(self, tarea):
        print(f"El profesor {self.nombre} ha asignado la tarea {tarea}")


class Ingeniero(Ciudadano):
    def __init__(self, nombre, edad, campo, empresa):
        super().__init__(nombre, edad)
        self.campo = campo
        self.empresa = empresa

    def diseñar(self, proyecto):
        return f"El ingeniero {self.nombre} está diseñando {proyecto}"

    def solucionar_problema(self, problema):
        print(f"El ingeniero {self.nombre} ha solucionado el problema {problema}")


# Crear una función para validar los datos introducidos por el usuario

def validar_datos(nombre, edad, profesion):
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser una cadena de caracteres")
    if not isinstance(edad, int) or edad < 0:
        raise ValueError("La edad debe ser un número entero positivo")
    if profesion not in ("medico", "profesor", "ingeniero"):
        raise ValueError("La profesión debe ser médico, profesor o ingeniero")


# Crear una función para crear un ciudadano

def crear_ciudadano(nombre, edad, profesion):
    validar_datos(nombre, edad, profesion)
    if profesion == "medico":
        return Medico(nombre, edad, "", "")
    elif profesion == "profesor":
        return Profesor(nombre, edad, "", "")
    else:
        return Ingeniero(nombre, edad, "", "")


# Crear una función para crear una lista de ciudadanos

def crear_lista_ciudadanos():
    lista_ciudadanos = []
    with open("ciudadanos.txt", "r") as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            nombre, edad, profesion = linea
            lista_ciudadanos.append(crear_ciudadano(nombre, edad, profesion))
    return lista_ciudadanos


# Crear una función para mostrar la información de un ciudadano

def mostrar_informacion(ciudadano):
    print(f"Nombre: {ciudadano.nombre}")
    print(f"Edad: {ciudadano.edad}")
    if isinstance(ciudadano, Medico):
        print(f"Especialidad: {ciudadano.especialidad}")
        print(f"Hospital: {ciudadano.hospital}")
    elif isinstance(ciudadano, Profesor):
        print(f"Asignatura: {ciudadano.asignatura}")
        print(f"Colegio: {ciudadano.colegio}")
    else:
        print(f"Campo: {ciudadano.campo}")
        print(f"Empresa: {ciudadano.empresa}")


# Crear una función para mostrar la lista de ciudadanos

def mostrar_lista_ciudadanos(lista_ciudadanos):
    for ciudadano in lista_ciudadanos:
        mostrar_informacion(ciudadano)

