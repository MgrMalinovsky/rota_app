# Generated by Django 3.0.2 on 2020-02-24 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_work_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worktime',
            old_name='workday',
            new_name='date',
        ),
    ]