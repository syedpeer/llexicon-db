# Generated by Django 2.1.11 on 2019-12-15 18:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_auto_20191215_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created_by_author',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 18, 42, 24, 152457, tzinfo=utc)),
        ),
    ]