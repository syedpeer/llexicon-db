# Generated by Django 2.2.10 on 2020-04-09 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='show_footer',
            new_name='show_animated_background',
        ),
    ]
