from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inv.Shoppingcart import Carrito
from inv.models import Products
from pedido.models import User, Document
from pedido.form_entrega import FormEntrega, FormEditarEntrega
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from PQRS.models import Pqrs, type
from django.db import transaction

def index(request):
    return render(request, 'index.html')

def err403(request, exception):
    return render(request, '403.html', status=403)

def err404(request, exception):
    return render(request, '404.html', status=404)

def err505(request, exception):
    return render(request, 'Error505.html', status=500)

def inicio(request):
    productos = Products.objects.all()

    filtro = 0

    if request.method == 'POST':
        if 'hombres' in request.POST:
            filtro = 25
        elif 'mujeres' in request.POST:
            filtro = 26
        elif 'infantil' in request.POST:
            filtro = 27

    nombre_usuario = None
    es_superuser = False
    if request.user.is_authenticated:
        nombre_usuario = request.user
        es_superuser = nombre_usuario.is_superuser
        return render(request, 'inicio.html', {
            'filtro': filtro, 
            'productos': productos,
            'nombre_usuario': nombre_usuario,
            'es_superuser': es_superuser
        })
    else:
        return render(request, 'inicio.html', {
            'filtro': filtro, 
            'productos': productos
        })

@login_required
def vista_carrito(request):
    return render(request, 'Carrito.html', {})

@login_required
def agregar_prod_car(request, producto_id):
    carrito = Carrito(request)
    producto = Products.objects.get(id=producto_id)
    carrito.agregar_producto(producto)
    return redirect('inicio')

@login_required
def sumar_prod_car(request, producto_id):
    carrito = Carrito(request)
    producto = Products.objects.get(id=producto_id)
    carrito.agregar_producto(producto)
    return redirect('carrito')

@login_required
def eliminar_prod_car(request, producto_id):
    carrito = Carrito(request)
    producto = Products.objects.get(id=producto_id)
    carrito.eliminar_prod_carrito(producto)
    return redirect('carrito')

@login_required
def restar_prod_car(request, producto_id):
    carrito = Carrito(request)
    producto = Products.objects.get(id=producto_id)
    carrito.restar_productos(producto)
    return redirect('carrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect('carrito')

@login_required
def limpiar_carrito_inicio(request):
    carrito = Carrito(request)
    productos_carrito = carrito.carrito.values()

    with transaction.atomic():
        for producto_info in productos_carrito:
            producto_id = producto_info['producto_id']
            cantidad = producto_info['cantidad']
            producto = Products.objects.get(id=producto_id)

            producto.amount -= cantidad
            producto.save()
    carrito.limpiar_carrito()
    return redirect('inicio')

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Credenciales incorrectas o usuario inactivo. Por favor, inténtalo de nuevo.')
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')

def send_email_register(correo_enviar, nom_usuario):
    context = {'nom_usuario': nom_usuario}
    template = get_template('correo.html')
    content = template.render(context)
    correo = EmailMultiAlternatives(
        f'Bienvenido a Attire 😀',
        'Mejora tu estilo con todas nuestras prendas.',
        settings.EMAIL_HOST_USER,
        [correo_enviar]
    )
    correo.attach_alternative(content, 'text/html')
    correo.send()

def register_view(request):
    if request.method == 'POST':
        type_document_id = request.POST.get('type_document')
        number_document = request.POST.get('number_document')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if type_document_id and number_document and first_name and last_name and username and email and phone and password:
            type_document = Document.objects.get(pk=type_document_id)
            nuevo_usuario = User.objects.create_user(
                type_document = type_document,
                number_document = number_document,
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                phone = phone,
                password = password,
            )
            nuevo_usuario.set_password(password)
            nuevo_usuario.save()
            send_email_register(email, username)
            return redirect('login')
    tipos = Document.objects.all()
    return render(request, 'registro.html', {'tipos' : tipos})

# @login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def entrega_view(request):
    if request.method == 'POST':
        # Crear datos de entrega del usuario
        form_crear_entrega = FormEntrega(request.POST or None)
        if form_crear_entrega.is_valid() and request.POST:
            user = request.user
            user.address = form_crear_entrega.cleaned_data['address']
            user.zip_code = form_crear_entrega.cleaned_data['zip_code']
            user.locality = form_crear_entrega.cleaned_data['locality']
            user.save()
            return redirect('entrega')
        # Actualizar datos de entrega del usuario
        form_editar_entrega = FormEditarEntrega(request.POST or None)
        if form_editar_entrega.is_valid() and request.POST:
            user = request.user
            user.address = form_editar_entrega.cleaned_data['address']
            user.zip_code = form_editar_entrega.cleaned_data['zip_code']
            user.locality = form_editar_entrega.cleaned_data['locality']
            user.save()
            return redirect('entrega')
        
    else:
        form_crear_entrega = FormEntrega(instance=request.user)
        form_editar_entrega = FormEditarEntrega(instance=request.user)
    # Mostrar datos de entrega del usuario
    datos_usuario = None
    es_superuser = False

    if request.user.is_authenticated:
        datos_usuario = request.user
        es_superuser = datos_usuario.is_superuser
    return render(request, 'entrega.html', {
        'form_crear_entrega': form_crear_entrega,
        'datos_usuario': datos_usuario,
        'es_superuser': es_superuser,
        'form_editar_entrega': form_editar_entrega,
        })

@login_required
def delete_entrega_view(request, id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=id)
            user.delete()
        except User.DoesNotExist:
            pass
    return redirect('entrega')

@login_required
def finish_buy(request):
    datos_usuario = None
    es_superuser = False
    productos_carrito = []
    if request.user.is_authenticated:
        if 'carrito' in request.session.keys():
            carrito = Carrito(request)
            productos_carrito = carrito.carrito.values()
        datos_usuario = request.user
        es_superuser = datos_usuario.is_superuser
    return render(request, 'finalizar_compra.html', {
        'datos_usuario': datos_usuario,
        'es_superuser': es_superuser,
        'productos_carrito': productos_carrito
    })

@login_required
def pqrs_view(request):
    if request.method == 'POST':
        client = request.user
        tipo_pqrs = request.POST.get('pqrs_types')
        description = request.POST.get('description')
        if client and tipo_pqrs and description:
            tipqrs = type.objects.get(pk=tipo_pqrs)
            new_pqrs = Pqrs.objects.create(
                client = client,
                type = tipqrs,
                description = description,
            )
            new_pqrs.save()
            return redirect('pqrs')
    tipos_pqrs = type.objects.all()
    datos_usuario = None
    es_superuser = False
    if request.user.is_authenticated:
        datos_usuario = request.user
        es_superuser = datos_usuario.is_superuser
    return render(request, 'pqrs.html', {
        'datos_usuario': datos_usuario,
        'es_superuser': es_superuser,
        'tipos_pqrs': tipos_pqrs,
    })

@login_required
def mostrar_pqrs(request):
    datos_usuario = None
    es_superuser = False
    lista_pqrs = None
    if request.user.is_authenticated:
        datos_usuario = request.user
        es_superuser = datos_usuario.is_superuser
        lista_pqrs = Pqrs.objects.filter(client=request.user).order_by('-date')
    return render(request, 'mostrar_pqrs.html', {
        'datos_usuario': datos_usuario,
        'es_superuser': es_superuser,
        'lista_pqrs': lista_pqrs
    })

@login_required
def eliminar_pqrs(request, id):
    pqrs = Pqrs.objects.get(id=id)
    if request.user == pqrs.client:
        pqrs.delete()
        return redirect('mostrar_pqrs')