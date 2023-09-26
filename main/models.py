from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Cascade digunakan untuk apabila user yang memiliki banyak 
                                                             # products ini dihapus --> productsnya akan ikut terhapus
    name = models.CharField(max_length=255, name="name")
    amount = models.IntegerField(name="amount")
    description = models.TextField(name="description")
    price = models.IntegerField(name="price")
    date_added = models.DateField(auto_now_add=True, name="date_added")

    def __str__(self):
        return f"{self.name} {self.amount} {self.price} {self.date_added} {self.description}"