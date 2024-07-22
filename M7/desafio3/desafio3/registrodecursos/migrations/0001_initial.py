# Generated by Django 5.0.7 on 2024-07-22 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('version', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateTimeField(auto_now_add=True)),
                ('modificacion_registro', models.DateTimeField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
                ('cursos', models.ManyToManyField(related_name='estudiantes', to='registrodecursos.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('depto', models.CharField(max_length=10, null=True)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='direccion', to='registrodecursos.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateTimeField(auto_now_add=True)),
                ('modificacion_registro', models.DateTimeField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
                ('cursos', models.ManyToManyField(related_name='profesores', to='registrodecursos.curso')),
            ],
        ),
    ]
