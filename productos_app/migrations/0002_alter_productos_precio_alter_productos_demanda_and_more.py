# Generated by Django 4.2 on 2024-12-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Precio',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productos',
            name='demanda',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.CharField(max_length=100),
        ),
    ]
