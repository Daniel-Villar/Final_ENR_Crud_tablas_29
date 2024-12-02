# Generated by Django 4.2 on 2024-12-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('Precio', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('precio_mayoreo', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('demanda', models.IntegerField()),
                ('idSucursal', models.CharField(max_length=100)),
            ],
        ),
    ]