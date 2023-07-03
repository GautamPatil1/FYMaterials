from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def subjects(request):
    material = request.GET.get('material')
    return render(request, 'subjects.html', {'material': material})

def subject(request):
    subject = request.GET.get('subject')
    material = request.GET.get('material')
    return render(request, 'subject.html', {'subject': subject, 'material': material })