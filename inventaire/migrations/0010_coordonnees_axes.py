# Generated by Django 4.2.3 on 2024-02-14 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0009_alter_coordonnees_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordonnees',
            name='axes',
            field=models.ManyToManyField(default=[1], to='inventaire.axe'),
        ),
    ]
