class ProductoBase:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Bebida(ProductoBase):
    def __init__(self, nombre, precio, tamaño, tipo, opciones_personalizables):
        super().__init__(nombre, precio)
        self.tamaño = tamaño
        self.tipo = tipo
        self.opciones_personalizables = opciones_personalizables

class Postre(ProductoBase):
    def __init__(self, nombre, precio, es_vegano, es_sin_gluten):
        super().__init__(nombre, precio)
        self.es_vegano = es_vegano
        self.es_sin_gluten = es_sin_gluten

class Inventario:
    def __init__(self):
        self.ingredientes = {}

    def agregar_ingrediente(self, nombre, cantidad):
        if nombre in self.ingredientes:
            self.ingredientes[nombre] += cantidad
        else:
            self.ingredientes[nombre] = cantidad

    def verificar_stock(self, producto):
        if isinstance(producto, Bebida):
            for ingrediente in producto.opciones_personalizables:
                if self.ingredientes.get(ingrediente, 0) <= 0:
                    return False
        return True

class Pedido:
    def __init__(self):
        self.productos = []
        self.estado = "pendiente"
        self.total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        self.total = sum(producto.precio for producto in self.productos)
        return self.total

    def validar_stock(self, inventario):
        for producto in self.productos:
            if isinstance(producto, Bebida):
                if not inventario.verificar_stock(producto):
                    return False
        return True

    def __str__(self):
        self.calcular_total()
        productos_str = ', '.join([producto.nombre for producto in self.productos])
        return f"🛍️ Productos: [{productos_str}], 💰 Total: ${self.total:.2f}, 📦 Estado: {self.estado}"

class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.historial = []

    def realizar_pedido(self, pedido):
        self.historial.append(pedido)
        pedido.estado = "completado"
        print(f"🎉 Pedido realizado por {self.nombre}: {pedido}")

class Empleado:
    def __init__(self, nombre, correo, rol):
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def actualizar_inventario(self, inventario, producto, cantidad):
        inventario.agregar_ingrediente(producto.nombre, cantidad)

# Crear inventario
inventario = Inventario()
inventario.agregar_ingrediente("café", 10)
inventario.agregar_ingrediente("leche", 5)
inventario.agregar_ingrediente("azúcar", 20)

# Crear productos
bebida1 = Bebida("Café con leche", 3.50, "mediano", "caliente", ["leche", "azúcar"])
postre1 = Postre("Brownie", 2.00, True, False)

# Crear cliente
cliente1 = Cliente("Juan Pérez", "juan@example.com")

# Crear pedido
pedido1 = Pedido()
pedido1.agregar_producto(bebida1)
pedido1.agregar_producto(postre1)

# Validar stock antes de proceder con el pedido
if pedido1.validar_stock(inventario):
    cliente1.realizar_pedido(pedido1)
else:
    print("🚫 No hay suficiente stock para completar el pedido.")

# Actualizar inventario (ejemplo)
empleado1 = Empleado("Ana Gómez", "ana@example.com", "barista")

# Crear productos en inventario
cafe = ProductoBase("café", 0)
leche = ProductoBase("leche", 0)

empleado1.actualizar_inventario(inventario, cafe, -1)
empleado1.actualizar_inventario(inventario, leche, -1)

# Imprimir estado del pedido
print("\n📋 Estado del Pedido:")
print(pedido1)