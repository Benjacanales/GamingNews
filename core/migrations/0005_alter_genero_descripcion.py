# Generated by Django 5.0.4 on 2024-05-16 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_genero_usuario_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='descripcion',
            field=models.CharField(default='No Especificado', max_length=10),
        ),
    ]
