# Generated by Django 4.2.7 on 2023-11-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='post_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
