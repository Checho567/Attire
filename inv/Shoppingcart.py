from django.contrib.sites import requests

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            self.session['carrito'] = {}
            self.carrito = self.session['carrito']
        else:
            self.carrito = carrito

    def agregar_producto(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                'producto_id': producto.id,
                'foto': producto.photo,
                'nombre': producto.name,
                'precio': producto.cost,
                'cantidad': 1
            }
        else:
            self.carrito[id]['cantidad'] += 1
            self.carrito[id]['precio'] += producto.cost
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar_prod_carrito(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar_productos(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['precio'] -= producto.cost
            if self.carrito[id]['cantidad'] <= 0: self.eliminar_prod_carrito(producto)
            self.guardar_carrito()

    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True

    def total_iva(self):
        total = sum(float(item['precio']) for item in self.carrito.values())
        iva = total * 0.19
        return iva

    def total_a_pagar(self):
        total_productos = sum(float(item['precio']) for item in self.carrito.values())
        iva = total_productos * 0.19
        total_a_pagar = total_productos + iva
        return total_a_pagar