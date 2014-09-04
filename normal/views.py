# Create your views here.
# coding: UTF-8
from django.shortcuts import render_to_response, render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from backend.utility import handle_uploaded_file
from backend.logging import loginfo
from users.models import *
from users.form import NormalUserForm
from normal.form import *
from normal.models import *
from normal.utility import upload_save_process,upload_preimage
@login_required()
def index(request):
    normalprofile = NormalProfile.objects.get(userid = request.user)
    filehistory = VideoSubmisson.objects.filter( normalfile_id = normalprofile)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR'] 
	print ip
    data = {
            "filehistory":filehistory,
            "normalid":normalprofile.id,
           }

    return render(request,'normal/normalhome.html',data)


@login_required()
def upload(request):
    normalprofile = NormalProfile.objects.get(userid = request.user)
    filehistory = VideoSubmisson.objects.filter( normalfile_id = normalprofile)
    if request.method=="POST":
        try:
            obj = upload_save_process(request,normalprofile)
            preimage = upload_preimage(request,obj)
            return HttpResponseRedirect('/normal/')
        except Exception, e:
            print e
        
    data = {
		   	"filehistory":filehistory,
            "normalid":normalprofile.id,
		   }
    return render(request,'normal/upload.html',data)

def accountsetting(request):
    normalprofile = NormalProfile.objects.get(userid = request.user)
    if request.method =="POST":
        print "haha"
        normalUserForm = NormalUserForm(request.POST,instance = normalprofile)
        if normalUserForm.is_valid():
            normalUserForm.save()
            print "hha"
            return HttpResponseRedirect('/normal/')
        else:
            print normalUserForm.errors
    else:
        normalUserForm = NormalUserForm(instance=normalprofile)
    
    data = {
        'normalUserForm':normalUserForm,
    }
    return render(request,'normal/accountsetting.html',data)
def replay(request,pid):
    video = VideoSubmisson.objects.get(file_id = pid )
    print pid
    data = {
        'video':video,
    }
    return render(request,'replay/test.html',data)
