# Generated by Django 5.1.2 on 2024-11-10 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0003_alter_exercise_allowed_weights_free_weight_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='exercise',
            table='Exercise',
        ),
        migrations.AlterModelTable(
            name='muscle',
            table='Muscle',
        ),
    ]
