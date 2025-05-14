from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.

def index(request):
    return render(request, 'todo/index.html')

def home(request):
    return render(request, 'home.html')

class HomeView(View):
    ...