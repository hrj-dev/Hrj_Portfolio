from django.http import HttpResponse
from django.shortcuts import render
from .models import about,slider,client


def home(request):
     aboutdata = about.objects.all()[0]
     sliderdata = slider.objects.all()
     clientdata = client.objects.all()

     context ={
          'about': aboutdata,
          'slider': sliderdata,
          'client': clientdata
     }
     return render(request, 'employee/index.html',context)

def aboutus(request):
     return render(request,'employee/about.html')

