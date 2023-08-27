from django.shortcuts import render
from django.http import HttpResponse

def movies(request):
    return render(request, 'movies.html')

