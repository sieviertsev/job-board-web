from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.getById, name = 'getVacancyById'),
    path('list', views.getMany, name = 'getManyVacancies'),
    path('getAllByUser', views.getAllByUser, name = 'getAllByUser'),
    path('create', views.create, name = 'createVacancy'),
    path('delete/<int:id>/', views.delete, name = 'deleteVacancy'),
]