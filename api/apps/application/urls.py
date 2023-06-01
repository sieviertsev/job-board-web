from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.getById, name = 'getApplicationById'),
    path('list', views.getMany, name = 'getManyApplications'),
    path('create', views.create, name = 'createApplication'),
    path('delete/<int:id>/', views.delete, name = 'deleteApplication'),
]