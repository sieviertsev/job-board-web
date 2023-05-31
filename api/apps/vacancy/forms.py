from django import forms
from .models import Vacancy

class CreateVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ["name", "description"]