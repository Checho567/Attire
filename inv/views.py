from django.shortcuts import render
from .models import Products

def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    return render(request, 'inicio.html', {'product': product})