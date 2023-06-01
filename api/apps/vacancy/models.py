from django.db import models
from django.contrib.auth.models import User

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
