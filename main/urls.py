from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'), 
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:pk>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:pk>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('increment-ajax/<int:pk>/', increment_ajax, name='increment_ajax'),
    path('decrement-ajax/<int:pk>/', decrement_ajax, name='decrement_ajax'),
    path('delete-ajax/<int:pk>/', delete_ajax, name='delete_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]