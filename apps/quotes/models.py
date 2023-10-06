from django.db import models
from django.utils import timezone
# Create your models here.

class Log(models.Model):
    time = models.DateTimeField(default=timezone.now)
    type = models.CharField(default="", max_length=100, blank=False, null=False)
    location = models.CharField(default="",max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)