# Generated by Django 5.0 on 2023-12-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_car_notation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='notation',
            field=models.IntegerField(null=True, verbose_name='Note'),
        ),
    ]
