# Create your views here.
# coding: UTF-8
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect 
from backend.utility import handle_uploaded_file
from users.models import *
from normal.form import *
from normal.models import *
from normal.utility import upload_save_process
def index(request):
    return render(request,'normal/normalhome.html')

def upload(request):
    normalprofile = NormalProfile.objects.get(userid = request.user)
    filehistory = VideoSubmisson.objects.filter( normalfile_id = normalprofile)
    if request.method=="POST":
        upload_save_process(request,normalprofile)
        print request.POST['title']
        return HttpResponseRedirect('/normal/')
        
    data = {
		   	"filehistory":filehistory,
            "normalid":normalprofile.id,
		   }
    return render(request,'normal/upload.html',data)
