from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def homeview(request):
    return render(request,'landing.html')