from django.shortcuts import render
from  django.http import HttpResponse
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'portfolio_website/index.html', {'courses':courses} )

def  detail(request, id):
    print(id)
    return render(request,'portfolio_website/index.html')

  