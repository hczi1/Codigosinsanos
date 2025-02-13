from datetime import date

class Material:
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado  # "disponible" o "prestado"

class Libro(Material):
    def __init__(self, nombre, autor, genero):
        super().__init__(nombre, "disponible")
        self.autor = autor
        self.genero = genero

class Revista(Material):
    def __init__(self, nombre, edicion, periodicidad):
        super().__init__(nombre, "disponible")
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, nombre, tipo_archivo, enlace_descarga):
        super().__init__(nombre, "disponible")
        self.tipo_archivo = tipo_archivo
        self.enlace_descarga = enlace_descarga

class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

class Usuario(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.materiales_prestados = []

    def consultar_catalogo(self, catalogo):
        return catalogo

class Bibliotecario(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)

    def agregar_material(self, sucursal, material):
        sucursal.catalogo.append(material)
        print(f"📚 {material.nombre} ha sido agregado al catálogo de {sucursal.nombre}.")

    def gestionar_prestamos(self, usuario, material):
        if material.estado == "disponible":
            material.estado = "prestado"
            usuario.materiales_prestados.append(material)
            print(f"✅ {usuario.nombre} ha prestado {material.nombre}.")
        else:
            print(f"🚫 {material.nombre} no está disponible para préstamo.")

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []

class Prestamo:
    def __init__(self, usuario, material, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class Penalizacion:
    def __init__(self, usuario, monto):
        self.usuario = usuario
        self.monto = monto

class Catalogo:
    def __init__(self, sucursal):
        self.sucursal = sucursal

    def buscar_materiales(self, criterio):
        resultados = []
        for material in self.sucursal.catalogo:
            if (isinstance(material, Libro) and material.autor == criterio) or \
               (isinstance(material, Revista) and material.edicion == criterio) or \
               (isinstance(material, MaterialDigital) and material.tipo_archivo == criterio):
                resultados.append(material)
        return resultados

# Ejemplo de uso
# Crear sucursal
sucursal1 = Sucursal("Sucursal Central")

# Crear materiales
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción")
revista1 = Revista("National Geographic", "Edición de enero", "Mensual")
material_digital1 = MaterialDigital("Curso de Python", "PDF", "http://ejemplo.com/curso-python")

# Agregar materiales a la sucursal
bibliotecario = Bibliotecario("Ana Gómez", "ana@example.com")
bibliotecario.agregar_material(sucursal1, libro1)
bibliotecario.agregar_material(sucursal1, revista1)
bibliotecario.agregar_material(sucursal1, material_digital1)

# Crear usuario
usuario1 = Usuario("Juan Pérez", "juan@example.com")

# Consultar catálogo
catalogo = Catalogo(sucursal1)
print("\n📖 Catálogo de la Sucursal:")
for material in sucursal1.catalogo:
    print(f"- {material.nombre} ({material.estado})")

# Realizar un préstamo
prestamo1 = Prestamo(usuario1, libro1, date.today(), None)
bibliotecario.gestionar_prestamos(usuario1, libro1)

# Imprimir estado del préstamo
print(f"\n📋 Estado del préstamo:")
print(f"Usuario: {prestamo1.usuario.nombre}, Material: {prestamo1.material.nombre}, Fecha de préstamo: {prestamo1.fecha_prestamo}")

# Verificar penalización (ejemplo simplificado)
penalizacion1 = Penalizacion(usuario1, 5.0)  # Multa de 5.0 por retraso
print(f"\n💰 Penalización para {penalizacion1.usuario.nombre}: ${penalizacion1.monto}")