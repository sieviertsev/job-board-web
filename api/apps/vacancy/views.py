from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Vacancy
from .forms import CreateVacancyForm

def getMany(request):
    vacancies = Vacancy.objects.all()

    context = {'vacancies': vacancies}

    return render(request, 'vacancy/list-of-vacancies.html', context)

def getById(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)

    context = {'vacancy': vacancy}

    return render(request, 'vacancy/vacancy-details.html', context)


@login_required(login_url='signIn')
def create(request):
    form = CreateVacancyForm()

    if request.method == 'POST':
        form = CreateVacancyForm(request.POST)
        if form.is_valid():
            vacancy = Vacancy(
                name=form.cleaned_data['name'], 
                description=form.cleaned_data['description'],
                employer=request.user
            )
            vacancy.save()
            messages.info(request, 'Vacancy created')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect values')
    
    context = {'form': form}

    return render(request, 'vacancy/create-vacancy.html', context)


@login_required(login_url='signIn')
def delete(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)

    if vacancy.employer.id != request.user.id:
        messages.error(request, 'Access denied')
        return redirect('home')

    vacancy.delete()
    messages.info(request, 'Vacancy deleted')

    return redirect('home')

