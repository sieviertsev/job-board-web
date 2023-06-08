from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=100, default='')

    class Meta:
        app_label = 'vacancy'

class Vacancy(models.Model):
    class JobType(models.TextChoices):
        FULLTIME = "Full Time", _("Full Time")
        PARTTIME = "Part Time", _("Part Time")
        REMOTE = "Remote", _("Remote")
        FREELANCE = "Freelance", _("Freelance")
    
    name = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    price = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(100000)
        ])
    type = models.CharField(
        max_length=10,
        choices=JobType.choices,
    )
    description = models.TextField(max_length=1000)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'vacancy'
