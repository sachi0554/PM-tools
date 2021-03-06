# Generated by Django 3.2.6 on 2021-08-09 13:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210806_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='planned_task',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='release_no',
            field=models.CharField(default='0.0.0', max_length=5),
        ),
    ]
