# Generated by Django 5.0 on 2023-12-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_annee_alter_car_cylindree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='modele',
            field=models.CharField(max_length=45, verbose_name='Modèle'),
        ),
    ]
