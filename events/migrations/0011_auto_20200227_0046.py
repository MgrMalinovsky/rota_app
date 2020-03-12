# Generated by Django 3.0.2 on 2020-02-27 00:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0010_auto_20200227_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktime',
            name='workers',
        ),
        migrations.AddField(
            model_name='worktime',
            name='workers',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]