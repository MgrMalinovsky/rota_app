# Generated by Django 3.0.2 on 2020-02-26 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200224_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktime',
            name='workers',
            field=models.ManyToManyField(to='events.work_person'),
        ),
    ]