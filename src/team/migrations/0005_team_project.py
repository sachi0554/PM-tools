# Generated by Django 3.2.6 on 2021-08-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210809_0649'),
        ('team', '0004_rename_team_member_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ManyToManyField(to='project.Project'),
        ),
    ]