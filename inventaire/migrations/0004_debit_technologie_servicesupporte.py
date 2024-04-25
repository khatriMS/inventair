# Generated by Django 4.2.3 on 2024-02-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0003_remove_proprietaire_axe_proprietaire_axes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Technologie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSupporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('debits', models.ManyToManyField(to='inventaire.debit')),
            ],
        ),
    ]
