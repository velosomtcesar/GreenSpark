# Generated by Django 5.1.1 on 2024-09-22 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='idade',
            new_name='senha',
        ),
    ]