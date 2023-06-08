from django.shortcuts import render

from vacancy.models import Category


def home(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'base.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def vacancy_form(request):
    context = {}
    return render(request, 'vacancy_form.html', context)