from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    pname=models.CharField(max_length=100)
    pquantity=models.PositiveIntegerField()
