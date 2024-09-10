from django.db import models

# Create your models here.
class Visit(models.Model):
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateField(auto_now=True)
