# Generated by Django 2.1.11 on 2019-11-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20191108_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.FileField(upload_to=''),
        ),
    ]