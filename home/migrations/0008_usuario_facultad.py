# Generated by Django 2.0.6 on 2018-09-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_ip_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='facultad',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
