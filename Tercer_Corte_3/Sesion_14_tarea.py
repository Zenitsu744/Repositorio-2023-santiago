class Articulos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def validar_nombre_y_precio(nombre, precio):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una palabra, no un número")
        if not isinstance(precio, float):
            raise TypeError("El precio debe ser un número, no una palabra")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo, porque no se pueden vender cosas a pérdida")

class SinIva(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0

    def calcular_precio_bruto(self):
        return self.precio

class Iva5(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.05

    def calcular_precio_bruto(self):
        return self.precio * (1 + self.iva)

class Iva19(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.19

    def calcular_precio_bruto(self):
        return self.precio * (1 + self.iva)

def menu():
    lista_articulos = []
    with open("alimentos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio = linea.split(",")
            lista_articulos.append(Articulos.crear_articulo(nombre, precio))

    while True:
        print("¿Qué quieres hacer?")
        print("1. Ver todos los alimentos")
        print("2. Buscar un alimento")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "3":
            break

        if opcion == "1":
            for articulo in lista_articulos:
                print(f"El precio bruto del {articulo.nombre} es {articulo.calcular_precio_bruto()} y el valor del IVA es {articulo.precio * articulo.iva}")

        elif opcion == "2":
            nombre = input("¿Qué alimento quieres buscar?: ")
            for articulo in lista_articulos:
                if articulo.nombre == nombre:
                    print(f"El precio bruto del {articulo.nombre} es {articulo.calcular_precio_bruto()} y el valor del IVA es {articulo.precio * articulo.iva}")
                    break
            else:
                print("No se encontró el alimento")

def main():
    menu()


if __name__ == "__main__":
    main()
