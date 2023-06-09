from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator

from SPARQLWrapper import SPARQLWrapper, JSON

from .models import Vacancy, Category
from .forms import CreateVacancyForm

def getMany(request):
    categoryId = request.GET.get('category')
    priceFrom = request.GET.get('priceFrom')
    priceTo = request.GET.get('priceTo')
    types = request.GET.getlist('type')

    vacancies = Vacancy.objects.all()
    vacanciesCount = vacancies.__len__

    if categoryId:
        vacancies = vacancies.filter(category_id=categoryId)

    if priceFrom and priceTo:
        vacancies = vacancies.filter(price__range=(priceFrom, priceTo))
    elif priceFrom:
        vacancies = vacancies.filter(price__gte=priceFrom)
    elif priceTo:
        vacancies = vacancies.filter(price__lte=priceTo)

    if types:
        vacancies = vacancies.filter(type__in=types)


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
        'vacanciesCount': vacanciesCount
    }

    return render(request, 'vacancy/list-of-vacancies.html', context)

def getById(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)

    agencyInfo = get_data(f'http://dbpedia.org/resource/{vacancy.agency}')

    context = {
        'vacancy': vacancy,
        'agencyInfo': agencyInfo[:500],
    }

    return render(request, 'vacancy/vacancy-details.html', context)

@login_required(login_url='signIn')
def getAllByUser(request):
    user = request.user
    vacancies = Vacancy.objects.filter(employer_id=user.id)

    current_time = timezone.now()

    for  vacancy in vacancies:
        time_difference = current_time - vacancy.created_at
        hours_ago = time_difference.total_seconds() // 3600
        vacancy.time_ago = f'{hours_ago} hours ago'
        if (hours_ago < 1):
            vacancy.time_ago = 'just now'
    
    context = {
        'vacancies': vacancies,
    }

    return render(request, 'vacancy/get-vacancies-by-user.html', context)


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

def get_data(url):
    endpoint_url = "https://dbpedia.org/sparql"
    query = f"""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>

        SELECT ?abstract WHERE {{
            <{url}> dbo:abstract ?abstract.
            FILTER (lang(?abstract) = 'en')
        }}
    """
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    abstract = ""
    if "results" in results and "bindings" in results["results"] and len(results["results"]["bindings"]) > 0:
        abstract = results["results"]["bindings"][0]["abstract"]["value"]
    
    return abstract
