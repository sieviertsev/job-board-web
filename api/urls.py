from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name = 'home'),

    path('about/', views.about, name = 'about'),

    path('contact/', views.contact, name = 'contact'),

    path('user/', include('user.urls')),

    path('vacancy/', include('vacancy.urls')),

    path('application/', include('application.urls')),
]
