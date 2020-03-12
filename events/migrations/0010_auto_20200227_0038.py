# Generated by Django 3.0.2 on 2020-02-27 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0009_auto_20200227_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktime',
            name='workers',
        ),
        migrations.AddField(
            model_name='worktime',
            name='workers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='work_person',
        ),
    ]