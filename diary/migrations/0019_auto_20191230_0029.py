# Generated by Django 2.1.11 on 2019-12-30 00:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0018_auto_20191230_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created_by_author',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 0, 29, 21, 45641, tzinfo=utc)),
        ),
    ]
