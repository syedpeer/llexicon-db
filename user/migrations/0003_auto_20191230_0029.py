# Generated by Django 2.1.11 on 2019-12-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_setting_full_container_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='full_container_width',
            field=models.BooleanField(default=False),
        ),
    ]
