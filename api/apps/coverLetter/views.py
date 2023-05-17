from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! It`s cover letter!')
