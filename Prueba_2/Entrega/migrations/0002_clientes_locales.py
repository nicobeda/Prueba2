# Generated by Django 4.2.6 on 2023-10-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Locales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=15)),
            ],
        ),
    ]
