# Generated by Django 3.0.2 on 2020-02-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='worktime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workday', models.DateField(verbose_name='date of work')),
            ],
        ),
    ]