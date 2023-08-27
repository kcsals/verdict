from django.shortcuts import render
from django.http import HttpResponse

def shows(request):
    return render(request, 'shows.html')
