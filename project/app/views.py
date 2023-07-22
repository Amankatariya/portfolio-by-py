from django.shortcuts import render,HttpResponse
from project import *
from .templates import *

# Create your views here.
def home(request):
    return render(request, 'home.html')