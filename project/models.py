from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField()
    clname=models.CharField(max_length=100)
