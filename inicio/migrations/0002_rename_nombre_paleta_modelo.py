# Generated by Django 4.2 on 2023-04-20 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paleta',
            old_name='nombre',
            new_name='modelo',
        ),
    ]
