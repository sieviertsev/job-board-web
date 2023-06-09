from django.contrib import admin

from .models import Vacancy, Category

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
