# Generated by Django 3.2.6 on 2021-08-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_team_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]