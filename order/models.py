from django.db import models

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    oname=models.CharField(max_length=100)
    oprice=models.PositiveIntegerField()
