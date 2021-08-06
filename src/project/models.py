from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Project(models.Model):

    methodology_options = [
        ('Agile', 'Agile'),
        ('Scrum', 'Scrum'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    methodology = models.CharField(choices=methodology_options, max_length=255)
    start_date =models.DateField(default=timezone.now)
    end_date =models.DateField(default=timezone.now)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)