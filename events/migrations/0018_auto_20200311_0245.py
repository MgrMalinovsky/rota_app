# Generated by Django 3.0.2 on 2020-03-11 02:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0017_auto_20200311_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workersinrota',
            name='workers',
            field=models.ManyToManyField(null=True, related_query_name='workers', to=settings.AUTH_USER_MODEL),
        ),
    ]
