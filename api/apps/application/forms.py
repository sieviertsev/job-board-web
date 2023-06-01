from django import forms
from .models import Application

class CreateApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "name", 
            "phone", 
            "aboutMe", 
            "workExperience", 
            "education", 
            "skills", 
            "coverLetter"
        ]