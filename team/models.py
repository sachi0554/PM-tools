from django.db import models
from django.conf import settings
from django.utils import timezone
from rest_framework.fields import ReadOnlyField

# Create your models here.


class TeamManager(models.Manager):

    def filter_by_instance(self, instance):
        obj_id = instance.id
        qs = super(TeamManager, self).filter(project= obj_id)
        return qs

class Team(models.Model):
    team_title = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    project =models.ManyToManyField(to='project.Project')
    team_description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = TeamManager()

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
        ('Front Developer', 'Front Developer'),
        ('Back End Developer', 'Back End Developer'),
        ('Team Lead', 'Team Lead'),
        ('Technical Head', 'Technical Head'),
        ('Project Manager', 'Project Manager'),
        ('DevOps', 'DevOps'),
        ('Database Engineer', 'Database Engineer'),
        ('Solution Architecture', 'Solution Architecture'),
         ('QA', 'QA'),
        ('Support Team', 'Support Team'),
         ('Business Annalists', 'Business Annalists'),
     ]
    dev_work_type = [
        ('Full Time', 'full_time'),
        ('Contract', 'contract'),
     ]

    dev_working_hours =[
        ('8 Hours', '8'),
        ('6 Hours', '6'),
        ('4 Hours', '4'),
        ('10 Hours', '10'),
         ('2 Hours', '2'),
    ]

    team =models.ForeignKey(Team, default=1, on_delete=models.CASCADE)
    full_name= models.CharField(max_length=255, blank=False, default='')
    dev_title = models.CharField(choices=dev_type, max_length=255)
    job_description = models.TextField()
    work_type = models.CharField(choices=dev_work_type, max_length=255)
    work_hours = models.CharField(choices=dev_working_hours, max_length=255)
    start_date =models.DateField(default=timezone.now)
    end_date =models.DateField(default=timezone.now)

    objects = MemberManager()