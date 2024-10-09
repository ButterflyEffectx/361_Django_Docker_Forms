from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return render(request, 'display.html')

# Create your views here.
