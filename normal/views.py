# Create your views here.
# coding: UTF-8
from django.shortcuts import render_to_response, render

def index(request):
    return render(request,'normal/normalhome.html')