# Generated by Django 2.1.11 on 2019-11-29 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAuthentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=256)),
                ('provider_id', models.CharField(max_length=256, unique=True)),
                ('access_token', models.TextField()),
                ('expires_in', models.CharField(max_length=256)),
                ('expires_at', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('picture', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SocialAuthentications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Social Provider',
                'verbose_name_plural': 'Social Providers',
                'ordering': ('-user_id',),
            },
        ),
    ]
