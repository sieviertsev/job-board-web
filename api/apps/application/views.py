from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Application
from .forms import CreateApplicationForm
from vacancy.models import Vacancy

def getMany(request, vacancyId):
    applications = Application.objects.filter(vacancy_id=vacancyId)

    context = {'applications': applications}

    return render(request, 'application/list-of-applications.html', context)

def getById(request, id):
    application = get_object_or_404(Application, id=id)

    context = {'application': application}

    return render(request, 'application/application-details.html', context)


@login_required(login_url='signIn')
def create(request, vacancyId):
    form = CreateApplicationForm()

    if request.method == 'POST':
        form = CreateApplicationForm(request.POST)
        if form.is_valid():
            vacancy = get_object_or_404(Vacancy, id=vacancyId)

            application = Application(
                name = form.cleaned_data['name'],
                phone = form.cleaned_data['phone'],
                aboutMe = form.cleaned_data['aboutMe'],
                workExperience = form.cleaned_data['workExperience'],
                education = form.cleaned_data['education'],
                skills = form.cleaned_data['skills'],
                coverLetter = form.cleaned_data['coverLetter'],
                user = request.user,
                vacancy = vacancy,
            )

            application.save()
            messages.info(request, 'Application created')
            return redirect('home')
        else:
            messages.error(request, form.errors)
    
    context = {'form': form}

    return render(request, 'application/create-application.html', context)


@login_required(login_url='signIn')
def delete(request, id):
    application = get_object_or_404(Application, id=id)

    if application.user.id != request.user.id:
        messages.error(request, 'Access denied')
        return redirect('home')

    application.delete()
    messages.info(request, 'Application deleted')

    return redirect('home')

