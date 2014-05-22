# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext
def index(request):
    print "haha"
    return render_to_response('base/base.html',context_instance=RequestContext(request)) 