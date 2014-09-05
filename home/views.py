# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext

from normal.models import *

import datetime

def index(request):
    filehistory = VideoSubmisson.objects.order_by('name').all()
    year = datetime.datetime.now().year
    data = {
        'filehistory':filehistory,
        'year': year,
    }
    return render(request,'home/home.html',data) 
