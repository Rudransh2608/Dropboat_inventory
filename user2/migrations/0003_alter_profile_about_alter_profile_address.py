# Generated by Django 5.0.1 on 2024-03-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user2', '0002_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='About',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]