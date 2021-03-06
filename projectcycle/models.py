from django.db import models

from django.utils import timezone


# Create your models here.


class ProjectCycleManager(models.Manager):
     

    def filter_by_instance(self, instance):
        obj_id = instance.id
        qs = super(ProjectCycleManager, self).filter(project= obj_id)
        return qs


class ProjectCycle(models.Model):
    title = models.CharField(max_length=255)
    project =models.ManyToManyField(to='project.Project')
    start_date =models.DateField(default=timezone.now)
    end_date =models.DateField(default=timezone.now)
    total_working_days = models.IntegerField(default=0)
    total_story_committed = models.IntegerField(default=0)
    total_story_completed = models.IntegerField(default=0)
    no_resource = models.IntegerField(default=0)
    planned_resource_hrs = models.IntegerField(default=0)
    average_resource_hrs = models.IntegerField(default=0)
    total_efforts = models.IntegerField(default=0)
    total_efforts_used = models.IntegerField(default=0)
    total_storypoints = models.IntegerField(default=0)
    total_storypoints_achieved = models.IntegerField(default=0)
    total_bugs_report_qa = models.IntegerField(default=0)
    total_bugs_report_valid_qa = models.IntegerField(default=0)
    total_bugs_report_prod = models.IntegerField(default=0)
    total_bugs_report_valid_prod = models.IntegerField(default=0)
    total_bugs_resolved_qa = models.IntegerField(default=0)
    total_bugs_resolved_prod = models.IntegerField(default=0)
    comments = models.TextField()
    isclose= models.BooleanField(default=False)
    objects = ProjectCycleManager()

