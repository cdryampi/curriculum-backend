# Generated by Django 5.0.4 on 2024-06-10 21:18

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia_manager', '0004_alter_mediafile_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='creado_por',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Data de creació'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, help_text='Data de modificació'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='modificado_por',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
