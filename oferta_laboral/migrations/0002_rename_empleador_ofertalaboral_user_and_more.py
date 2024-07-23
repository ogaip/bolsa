# Generated by Django 5.0.7 on 2024-07-21 20:06

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oferta_laboral', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ofertalaboral',
            old_name='empleador',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='ofertalaboral',
            name='beneficios',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='ofertalaboral',
            name='descripcion',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='ofertalaboral',
            name='estado',
            field=models.CharField(choices=[('Publicada', 'Publicada'), ('No Publicada', 'No Publicada')], default='Publicada'),
        ),
        migrations.AlterField(
            model_name='ofertalaboral',
            name='habilidades_requeridas',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='ofertalaboral',
            name='requisitos_laborales',
            field=tinymce.models.HTMLField(),
        ),
    ]
