from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    staff=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=100,null=True)
    phone=models.PositiveIntegerField(null=True)
    About=models.CharField(max_length=100,null=True)