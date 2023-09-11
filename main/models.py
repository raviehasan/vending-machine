from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, name="name")
    amount = models.IntegerField(name="amount")
    description = models.TextField(name="description")
    price = models.IntegerField(name="price")
    date_added = models.DateField(auto_now_add=True, name="date_added")