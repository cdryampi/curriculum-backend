# Generated by Django 5.0.4 on 2024-05-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0002_staticpage_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
