# Generated by Django 5.0.1 on 2024-03-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('oname', models.CharField(max_length=100)),
                ('oprice', models.PositiveIntegerField()),
            ],
        ),
    ]
