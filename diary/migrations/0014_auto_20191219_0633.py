# Generated by Django 2.1.11 on 2019-12-19 06:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0013_auto_20191219_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created_by_author',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 6, 33, 0, 885757, tzinfo=utc)),
        ),
    ]