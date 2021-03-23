# Generated by Django 3.1.5 on 2021-03-27 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='crated',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='updated',
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='ServiciosApp'),
        ),
    ]