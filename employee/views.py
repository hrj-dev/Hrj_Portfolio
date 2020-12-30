from django.shortcuts import render
from django.http import HttpResponse

def employee(request):
    return HttpResponse("this is the employee page")

def profile(request):
    return render(request,'employee/profile.html')

