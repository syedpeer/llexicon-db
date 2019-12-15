# Generated by Django 2.1.11 on 2019-12-15 00:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20191209_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created_by_author',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 0, 58, 36, 113431, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=18, null=True),
        ),
    ]
