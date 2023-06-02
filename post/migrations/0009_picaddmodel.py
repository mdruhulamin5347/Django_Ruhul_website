# Generated by Django 4.1.1 on 2023-05-20 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_rename_paren_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='picaddmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/image')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='post.post_model')),
            ],
        ),
    ]
