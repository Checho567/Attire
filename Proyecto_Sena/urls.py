"""
URL configuration for Proyecto_Sena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('admin/index/', admin.site.urls, name='admin:index'),    
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('403/', views.err403, name='403'),
    path('404/', views.err404, name='404'),
    path('505/', views.err505, name='505'),
    path('inicio/principal/', views.inicio, name='inicio'),
    path('carrito/', views.vista_carrito, name='carrito'),
    path('agregar/<int:producto_id>/', views.agregar_prod_car, name='agregar_prod'),
    path('sumar/<int:producto_id>/', views.sumar_prod_car, name='sumar_prod'),
    path('eliminar/<int:producto_id>/', views.eliminar_prod_car, name='eliminar_prod'),
    path('restar/<int:producto_id>/', views.restar_prod_car, name='restar_prod'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_car'),
    path('login/', LoginView.as_view(template_name='Login.html'), name='login'),
    path('registro/', views.register_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('entrega/', views.entrega_view, name='entrega'),
    path('pqrs/', views.pqrs_view, name='pqrs'),
    path('tus/pqrs', views.mostrar_pqrs, name='mostrar_pqrs'),
    path('pqrs/<int:id>/', views.eliminar_pqrs, name='eliminar_pqrs'),
    path('compra/finalizada/', views.finish_buy, name='comprater'),
    path('limiar/inicio/', views.limpiar_carrito_inicio, name='limiar_carrito_inicio')
]
