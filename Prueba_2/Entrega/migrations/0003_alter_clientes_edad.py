# Generated by Django 4.2.6 on 2023-10-05 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrega', '0002_clientes_locales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='edad',
            field=models.IntegerField(max_length=15),
        ),
    ]
