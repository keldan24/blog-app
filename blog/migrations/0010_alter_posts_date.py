# Generated by Django 4.2.7 on 2023-11-29 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 11, 13, 19, 645927)),
        ),
    ]
