# Generated by Django 3.2.6 on 2021-08-06 13:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_title', models.CharField(choices=[('Front Developer', 'front_end_dev'), ('Back End Developer', 'back_end_dev'), ('Team Lead', 'team_lead'), ('Technical Head', 'technical_head'), ('Project Manager', 'project_manage'), ('DevOps', 'devOps'), ('Database Designer', 'database_designer'), ('Support Team', 'support_team')], max_length=255)),
                ('job_description', models.TextField()),
                ('work_type', models.CharField(choices=[('Full Time', 'full_time'), ('Contract', 'contract')], max_length=255)),
                ('work_hours', models.CharField(choices=[('8 Hours', '8'), ('4 Hours', '4'), ('10 Hours', '8')], max_length=255)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.DeleteModel(
            name='TeamPlayer',
        ),
    ]
