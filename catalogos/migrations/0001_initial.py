# Generated by Django 3.2 on 2021-04-29 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laboratorio', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=70)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.area')),
            ],
        ),
    ]
