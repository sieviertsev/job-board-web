from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Application
from .forms import CreateApplicationForm

def getMany(request):
    applicayions = Application.objects.all()

    context = {'applications': applications}

    return render(request, 'application/list-of-applications.html', context)

def getById(request, id):
    vacancy = get_object_or_404(Application, id=id)

    context = {'application': application}

    return render(request, 'application/application-details.html', context)


@login_required(login_url='signIn')
def create(request):
    form = CreateApplicationForm()

    if request.method == 'POST':
        form = CreateApplicationForm(request.POST)
        if form.is_valid():
            application = Application(
                name=form.cleaned_data['name'], 
                details=form.cleaned_data['details'],
                employer=request.user ########################################################
            )
            application.save()
            messages.info(request, 'Application created')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect values')
    
    context = {'form': form}

    return render(request, 'application/create-application.html', context)


@login_required(login_url='signIn')
def delete(request, id):
    application = get_object_or_404(Application, id=id)

    if application.employer.id != request.user.id: ##################################################################################
        messages.error(request, 'Access denied')
        return redirect('home')

    application.delete()
    messages.info(request, 'Application deleted')

    return redirect('home')

