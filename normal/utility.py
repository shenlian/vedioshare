#!/usr/bin/env python
# coding: UTF-8
'''
 File Name: ./normal/utility.py
 Author: shenlian
 Created Time: 2014年05月28日 星期三 10时15分30秒
'''
import time
# import cv2
import os

from django.core.files.uploadedfile import UploadedFile
from normal.models import  VideoSubmisson,VideoPreImage
from backend.logging import loginfo

def upload_save_process(request,normalprofile):
	f = request.FILES["video"]
	name = request.POST["title"]
	wrapper_f = UploadedFile(f)
	filename = wrapper_f.name
	filetype = filename.split(".")[1]
	obj = VideoSubmisson()
	obj.name = name
	obj.file_obj = f
	obj.normalfile_id = normalprofile
	obj.uploadtime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
	obj.file_type = filetype
	obj.file_size = wrapper_f.file.size
	#TODO: we will check file type
	obj.file_type = filetype if filetype != " " else "unknown"
	try:		
		obj.save()
	except Exception,e:
		loginfo(p=e,label="error")
	loginfo(p=obj,label="obj")
	return obj

def upload_preimage(request,obj):
	pic = request.FILES["pic"]
	print obj.file_id
	try:	
		pic_obj = VideoPreImage()
		pic_obj.file_obj = pic
		pic_obj.video_id = obj
		pic_obj.uploadtime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
		pic_obj.save()
		loginfo(p=obj,label="obj")
	except Exception,e:
		print e
	return pic_obj

def save_preimage_process(request,videofile):
	"""
		处理视频程序运用opencv
	"""
	currenturl = os.path.dirname(os.path.abspath('__file__'))
	fileurl = str(videofile.file_obj)
	filepath = currenturl+'/media/'+fileurl
	print filepath
	videoCapture = cv2.VideoCapture(filepath)

	success, frame = videoCapture.read()
	count = 0  	
	while success:
		cv2.imshow("Oto video",frame)
		count = count + 1
		if count == 2000:
			print "2000"
			break
		success,frame = videoCapture.read()

