# Generated by Django 4.2.3 on 2024-02-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0002_proprietaire_axe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proprietaire',
            name='axe',
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='axes',
            field=models.ManyToManyField(default=[1], to='inventaire.axe'),
        ),
    ]
