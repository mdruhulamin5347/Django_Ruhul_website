# Generated by Django 4.1.1 on 2023-05-28 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_model',
            name='password',
        ),
    ]
