# Generated by Django 4.2 on 2024-11-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='idEmpleado',
            field=models.CharField(max_length=1, primary_key=True, serialize=False),
        ),
    ]
