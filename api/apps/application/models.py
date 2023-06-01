from django.db import models
from django.contrib.auth.models import User
from apps import Vacancy

class Application(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
