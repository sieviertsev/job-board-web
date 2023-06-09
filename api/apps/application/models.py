from django.db import models
from django.contrib.auth.models import User

from vacancy.models import Vacancy

class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    aboutMe = models.TextField(max_length=1000)
    workExperience = models.TextField(max_length=1000)
    education = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    coverLetter = models.TextField(max_length=2000)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
