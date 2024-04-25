# Generated by Django 4.2.3 on 2024-02-14 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0007_coordonnees_equipement_alter_coordonnees_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordonnees',
            name='longitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-20), django.core.validators.MaxValueValidator(-5)]),
        ),
    ]
