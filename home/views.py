# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext

from normal.models import *

def index(request):
    filehistory = VideoSubmisson.objects.all()
    data = {
        'filehistory':filehistory,
    }
    return render(request,'home/home.html',data) 