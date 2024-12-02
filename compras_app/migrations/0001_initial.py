# Generated by Django 4.2 on 2024-12-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('idCompra', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('idprovedor', models.CharField(max_length=6)),
                ('idEmpleado', models.CharField(max_length=6)),
                ('idProducto', models.CharField(max_length=6)),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_compra', models.DateField()),
            ],
        ),
    ]