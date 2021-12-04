from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
