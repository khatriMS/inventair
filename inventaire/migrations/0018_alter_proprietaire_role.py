# Generated by Django 5.0.2 on 2024-05-14 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0017_proprietaire_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proprietaire',
            name='role',
            field=models.CharField(choices=[('Option 1', 'Option 1'), ('Option 2', 'Option 2')], max_length=50),
        ),
    ]