from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name = 'home'),

    path('about/', views.about, name = 'about'),

    path('contact/', views.contact, name = 'contact'),

    path('vacancy_form/', views.vacancy_form, name = 'vacancy_form'),

    path('user/', include('user.urls')),

    path('vacancy/', include('vacancy.urls')),

    path('resume/', include('resume.urls')),

    path('coverLetter/', include('coverLetter.urls')),

    path('application/', include('application.urls')),
]
