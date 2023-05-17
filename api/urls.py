from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("user/signUp", views.signUp.as_view(), name='signUp'),
    path("user/signIn", views.signIn.as_view(), name='signIn'),
    path("user/update/{id}", views.userUpdate.as_view(), name='userUpdate'),

    path("vacancy/create", views.createVacancy.as_view(), name='createVacancy'),
    path("vacancies/", views.getAllVacancies.as_view(), name='getAllVacancies'),
    path("vacancy/update/{id}", views.vacancyUpdate.as_view(), name='vacancyUpdate'),
    path("vacancy/delete/{id}", views.vacancyDelete.as_view(), name='vacancyDelete'),

    path("resume/create", views.createResume.as_view(), name='createResume'),
    path("resume/{id}", views.getCertainResume.as_view(), name='getCertainResume'),
    path("resume/update/{id}", views.resumeUpdate.as_view(), name='resumeUpdate'),
    path("resume/delete/{id}", views.resumeDelete.as_view(), name='resumeDelete'),

    path("coverLetter/create", views.createCoverLetter.as_view(), name='createCoverLetter'),
    path("coverLetter/{id}", views.getCertainCoverLetter.as_view(), name='getCertainCoverLetter'),
    path("coverLetter/delete/{id}", views.coverLetterDelete.as_view(), name='coverLetterDelete'),

    path("applications/create", views.createApplication.as_view(), name='createApplication'),
    path("applications/{vacancyId}", views.getAllApplicationsByVacancy.as_view(), name='getAllApplicationsByVacancy'),
    path("applications/{id}", views.getCertainApplication.as_view(), name='getCertainApplication'),
    path("applications/delete/{id}", views.applicationDelete.as_view(), name='applicationDelete'),
]
