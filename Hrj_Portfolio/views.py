from django.http import HttpResponse
from django.shortcuts import render


def home(request):

     return render(request, 'employee/index.html',)

def about(request):
     return render(request,'employee/about.html')

def contact(request):
     return render(request,'employee/contact.html')
