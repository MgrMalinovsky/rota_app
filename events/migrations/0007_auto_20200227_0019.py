# Generated by Django 3.0.2 on 2020-02-27 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20200227_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='workers',
            field=models.ManyToManyField(to='events.work_person'),
        ),
    ]
