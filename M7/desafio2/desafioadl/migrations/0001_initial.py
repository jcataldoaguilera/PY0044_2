# Generated by Django 5.0.6 on 2024-06-24 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(default='')),
                ('eliminada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubTarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(default='')),
                ('eliminada', models.BooleanField(default=False)),
                ('tarea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desafioadl.tarea')),
            ],
        ),
    ]
