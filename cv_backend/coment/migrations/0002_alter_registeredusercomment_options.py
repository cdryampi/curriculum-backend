# Generated by Django 5.0.4 on 2024-06-10 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registeredusercomment',
            options={'permissions': [('can_create_guest_user_comment', 'Can create registered user comment'), ('can_edit_guest_user_comment', 'Can edit registered user comment'), ('can_delete_guest_user_comment', 'Can delete registered user comment')], 'verbose_name': 'Comentario de Usuario Registrado', 'verbose_name_plural': 'Comentarios de Usuarios Registrados'},
        ),
    ]
