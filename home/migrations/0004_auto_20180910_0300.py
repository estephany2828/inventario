# Generated by Django 2.0.6 on 2018-09-10 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180910_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nombreapellido',
            new_name='nombre',
        ),
    ]
