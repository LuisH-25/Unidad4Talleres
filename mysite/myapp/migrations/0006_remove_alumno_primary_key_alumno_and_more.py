# Generated by Django 4.1.3 on 2022-11-30 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alumno_primary_key_alumno'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='alumno',
            name='primary_key_alumno',
        ),
        migrations.AddConstraint(
            model_name='alumno',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='primary_key_alumno'),
        ),
    ]