# Generated by Django 5.0.4 on 2024-10-09 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('estado', models.IntegerField(default=1)),
                ('estado_civil', models.CharField(blank=True, max_length=50, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'apoderados',
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('estado', models.IntegerField(default=1)),
                ('estado_financiero', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('apoderado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matricula.apoderado')),
            ],
            options={
                'db_table': 'alumnos',
            },
        ),
    ]
