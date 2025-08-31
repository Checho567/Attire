from inv.Shoppingcart import Carrito


def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if 'carrito' in request.session.keys():
            for key, value in request.session['carrito'].items():
                total += float(value['precio'])
    return {'total_carrito': total}

def total_iva_carrito(request):
    total_iva = 0
    if request.user.is_authenticated:
        if 'carrito' in request.session.keys():
            carrito = Carrito(request)
            total_iva = carrito.total_iva()
    return {'total_iva_carrito': total_iva}

def total_a_pagar_carrito(request):
    total_a_pagar = 0
    if request.user.is_authenticated:
        if 'carrito' in request.session.keys():
            carrito = Carrito(request)
            total_a_pagar = carrito.total_a_pagar()
    return {'total_a_pagar_carrito': total_a_pagar}