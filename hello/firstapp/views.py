from django.shortcuts import render
from django.http import *


# Create your views here.
def index(request):
   return render(request,"firstapp/home.html")

#def index(request):
#    return HttpResponse("<h2> Главная </h2>")

def about(request):
    return HttpResponse("<h2> О сайте! </h2>")

def contact(request):
    return HttpResponse("<h2> Котакты: +7-926-102-54-29</h2>")