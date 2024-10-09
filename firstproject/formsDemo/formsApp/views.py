from django.shortcuts import render
from .forms import userRegisterForm

def userRegistrationView(request):
    form = userRegisterForm()
    return render(request, 'userRegistration.html',{'form':form})

def display(request):
    return render(request, 'display.html')
