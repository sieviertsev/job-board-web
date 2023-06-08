from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Vacancy, Category
from .forms import CreateVacancyForm

def getMany(request):
    vacancies = Vacancy.objects.all()
    categories = Category.objects.all()

    current_time = timezone.now()

    for  vacancy in vacancies:
        time_difference = current_time - vacancy.created_at
        hours_ago = time_difference.total_seconds() // 3600
        vacancy.time_ago = f'{hours_ago} hours ago'
        if (hours_ago < 1):
            vacancy.time_ago = 'just now'
    
    paginator = Paginator(vacancies, 3)
    page_number = request.GET.get('page')
    vacancies = paginator.get_page(page_number)

    context = {
        'vacancies': vacancies,
        'categories': categories,
    }

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
            category = get_object_or_404(Category, id=form.cleaned_data['categoryId'])
            vacancy = Vacancy(
                name=form.cleaned_data['name'], 
                agency=form.cleaned_data['agency'], 
                price=form.cleaned_data['price'], 
                type=form.cleaned_data['type'],
                description=form.cleaned_data['description'],
                employer=request.user,
                category=category,
            )
            vacancy.save()
            messages.info(request, 'Vacancy created')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect values')
    
    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories
    }

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

