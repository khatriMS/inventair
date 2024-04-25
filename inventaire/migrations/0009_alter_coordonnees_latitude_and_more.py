# Generated by Django 4.2.3 on 2024-02-14 22:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0008_alter_coordonnees_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordonnees',
            name='latitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-50), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='coordonnees',
            name='longitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-50), django.core.validators.MaxValueValidator(50)]),
        ),
    ]