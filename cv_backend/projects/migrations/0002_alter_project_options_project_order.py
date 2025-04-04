# Generated by Django 5.0.4 on 2025-03-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.IntegerField(default=0, help_text='Orden de visualización del proyecto.', verbose_name='Orden'),
        ),
    ]
