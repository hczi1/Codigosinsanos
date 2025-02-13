class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

class Usuario(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.reservas = [] 

    def hacer_reserva(self, funcion, asientos, promocion=None):  
        reserva = Reserva(self, funcion, asientos, promocion)
        if reserva.validar_asientos():
            self.reservas.append(reserva)
            reserva.confirmar_reserva()
        else:
            print(f"🚫 Asiento(s) {asientos} ocupado(s). No se pudo realizar la reserva.")

class Empleado(Persona):
    def __init__(self, nombre, email, rol):
        super().__init__(nombre, email)
        self.rol = rol

    def agregar_funcion(self, funcion):
        self.funcion = funcion

    def agregar_pelicula(self, pelicula):
        self.pelicula = pelicula

    def agregar_promocion(self, promocion):
        self.promocion = promocion

class Espacio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.disponibilidades = True

class Sala(Espacio):
    def __init__(self, nombre, capacidad, tipo):
        super().__init__(nombre, capacidad)
        self.tipo = tipo
        self.asientos_ocupados = []

    def reservar_asientos(self, asientos):
        for asiento in asientos:
            if asiento not in self.asientos_ocupados:
                self.asientos_ocupados.append(asiento)
            else:
                return False
        return True

class ZonaComida(Espacio):
    def __init__(self, nombre):
        super().__init__(nombre, capacidad=None) 
        self.productos = {}

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.calificacion = clasificacion
        self.genero = genero

class Promocion:
    def __init__(self, descripcion, descuento):
        self.descripcion = descripcion
        self.descuento = descuento

class Reserva:
    def __init__(self, usuario, funcion, asientos, promocion=None):
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.promocion = promocion

    def validar_asientos(self):
        return self.funcion.sala.reservar_asientos(self.asientos)  

    def confirmar_reserva(self):
        print(f"🎉 Reserva confirmada para {self.usuario.nombre} en la película '{self.funcion.pelicula.titulo}' en {self.funcion.sala.nombre}. Asientos reservados: {self.asientos}.")

class Funcion:
    def __init__(self, pelicula, sala, hora):
        self.pelicula = pelicula
        self.sala = sala
        self.hora = hora

# Pruebas
pelicula1 = Pelicula("Avatar", 162, "PG-13", "Ciencia Ficción")
pelicula2 = Pelicula("El Rey León", 88, "G", "Animación")

sala1 = Sala("Sala 1", 100, "2D")
sala2 = Sala("Sala 2", 150, "3D")

funcion1 = Funcion(pelicula1, sala1, "18:00")
funcion2 = Funcion(pelicula2, sala2, "20:00")

usuario1 = Usuario("Juan Pérez", "juan@example.com")

asientos_a_reservar = [1, 2, 3]  
usuario1.hacer_reserva(funcion1, asientos_a_reservar)  

empleado1 = Empleado("Ana Gómez", "ana@example.com", "administrador")
empleado1.agregar_funcion(funcion2)

asientos_b_reservar = [4, 5]  
usuario1.hacer_reserva(funcion2, asientos_b_reservar)  

# Intentar reservar asientos ocupados
asientos_c_reservar = [2, 3]  
usuario1.hacer_reserva(funcion1, asientos_c_reservar)  #