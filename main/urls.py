from django.urls import path
from main.views import show_main, show_products

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'), 
    path('products/', show_products, name='show_product')
]