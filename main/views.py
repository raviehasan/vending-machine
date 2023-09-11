from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all().values()
    context = {
        'name': 'Ravie Hasan Abud',
        'class': 'PBP A',
        'products' : products,
    }

    return render(request, "main.html", context)