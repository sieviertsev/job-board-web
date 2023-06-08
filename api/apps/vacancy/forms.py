from django import forms
from .models import Vacancy

class CreateVacancyForm(forms.ModelForm):
    categoryId = forms.IntegerField()

    class Meta:
        model = Vacancy
        fields = [
            "name", 
            "agency", 
            "price",
            "type",
            "description", 
        ]