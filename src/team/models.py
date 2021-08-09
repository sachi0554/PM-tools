from django.db import models
from django.conf import settings
from django.utils import timezone
from rest_framework.fields import ReadOnlyField

# Create your models here.
class Team(models.Model):
    team_title = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    team_description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    @property
    def Member(self):
        instance = self
        qs = Member.objects.filter_by_instance(instance)
        return qs

class MemberManager(models.Manager):
     

    def filter_by_instance(self, instance):
        obj_id = instance.id
        qs = super(MemberManager, self).filter(team= obj_id)
        return qs

class Member(models.Model):
    dev_type = [
        ('Front Developer', 'front_end_dev'),
        ('Back End Developer', 'back_end_dev'),
        ('Team Lead', 'team_lead'),
        ('Technical Head', 'technical_head'),
        ('Project Manager', 'project_manage'),
        ('DevOps', 'devOps'),
        ('Database Designer', 'database_designer'),
        ('Support Team', 'support_team'),
     ]
    dev_work_type = [
        ('Full Time', 'full_time'),
        ('Contract', 'contract'),
     ]

    dev_working_hours =[
        ('8 Hours', '8'),
        ('4 Hours', '4'),
        ('10 Hours', '8'),
    ]

    team =models.ForeignKey(Team, default=1, on_delete=models.CASCADE)
    dev_title = models.CharField(choices=dev_type, max_length=255)
    job_description = models.TextField()
    work_type = models.CharField(choices=dev_work_type, max_length=255)
    work_hours = models.CharField(choices=dev_working_hours, max_length=255)
    start_date =models.DateField(default=timezone.now)
    end_date =models.DateField(default=timezone.now)

    objects = MemberManager()