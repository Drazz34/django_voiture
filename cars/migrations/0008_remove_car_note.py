# Generated by Django 5.0 on 2023-12-07 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='note',
        ),
    ]
