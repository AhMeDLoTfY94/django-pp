# Generated by Django 3.1.5 on 2021-01-29 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_test_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]