#!/usr/bin/env python
# coding: UTF-8
'''
 File Name: ./normal/utility.py
 Author: shenlian
 Created Time: 2014年05月28日 星期三 10时15分30秒
'''
import time
import cv2
import os

from django.core.files.uploadedfile import UploadedFile
from normal.models import  VideoSubmisson,VideoPreImage
from backend.logging import loginfo

def upload_save_process(request,normalprofile):
	f = request.FILES["video"]
	pic = request.FILES["pic"]
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
	except BaseException,e:
		loginfo(p=e,label="error")

	pic_obj = VideoPreImage()
	pic_obj.file_obj = pic
	pic_obj.vedio_id = obj
	pic_obj.uploadtime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
	try:		
		pic_obj.save()
	except BaseException,e:
		loginfo(p=e,label="error")
#    save_preimage_process(request,obj)

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
		print "haha"
		count = count + 1
		if count == 2000:
			print "2000"
			break
		success,frame = videoCapture.read()

