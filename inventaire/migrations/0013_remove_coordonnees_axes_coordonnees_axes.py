# Generated by Django 4.2.3 on 2024-02-14 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0012_alter_coordonnees_axes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordonnees',
            name='axes',
        ),
        migrations.AddField(
            model_name='coordonnees',
            name='axes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventaire.axe'),
        ),
    ]
