from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'name': 'Ravie Hasan Abud',
        'class': 'PBP A',
        'student_id': '2206031864',
    }

    return render(request, "main.html", context)

def show_products(request):
    products = Product.objects.all().values()
    context = {
        'products' : products,
    }

    return render(request, "products.html", context)