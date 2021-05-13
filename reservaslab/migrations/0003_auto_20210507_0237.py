# Generated by Django 3.2.2 on 2021-05-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaslab', '0002_auto_20210502_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(max_length=70)),
            ],
        ),
        migrations.RenameField(
            model_name='reservaciones',
            old_name='horario',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='reservaciones',
            name='nombre_practica',
        ),
    ]
