# Generated by Django 2.0.6 on 2018-09-12 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_sala_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='departamento',
        ),
    ]
