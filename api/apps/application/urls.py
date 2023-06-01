from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.getById, name = 'getApplicationById'),
    path('list/<int:vacancyId>/', views.getMany, name = 'getManyApplications'),
    path('create/<int:vacancyId>/', views.create, name = 'createApplication'),
    path('delete/<int:id>/', views.delete, name = 'deleteApplication'),
]