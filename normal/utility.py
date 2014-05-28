#!/usr/bin/env python
# coding=utf-8
'''
 File Name: ./normal/utility.py
 Author: shenlian
 Created Time: 2014年05月28日 星期三 10时15分30秒
'''
import time

from django.core.files.uploadedfile import UploadedFile
from normal.models import  VideoSubmisson

def upload_save_process(request,normalprofile):
	f = request.FILES["pic"]
	wrapper_f = UploadedFile(f)
	filename = wrapper_f.name
	filetype = filename.split(".")[1]
	obj = VideoSubmisson()
	obj.name = request.POST['title']
	obj.file_obj = f
	obj.normalfile_id = normalprofile
	obj.uploadtime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
	obj.file_type = filetype
	obj.file_size = wrapper_f.file.size
	#TODO: we will check file type
	obj.file_type = filetype if filetype != " " else "unknown"
	obj.save()

