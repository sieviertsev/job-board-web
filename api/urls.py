from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),

    path('vacancy/', include('vacancy.urls')),

    path('resume/', include('resume.urls')),

    path('coverLetter/', include('coverLetter.urls')),

    path('application/', include('application.urls')),
]
