# Generated by Django 4.1.1 on 2023-04-09 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='paren',
            new_name='parent',
        ),
    ]