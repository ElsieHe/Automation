# Generated by Django 2.1.1 on 2018-10-05 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('platform_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='modification_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间'),
            preserve_default=False,
        ),
    ]
