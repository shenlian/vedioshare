#!/usr/bin/env python
# coding=utf-8
'''
 File Name: normal/admin.py
 Author: shenlian
 Created Time: 2014年06月01日 星期日 21时09分47秒
'''
from django.contrib import admin
from normal.models import VideoSubmisson,VideoPreImage

NormalRigsterSet = {
	VideoSubmisson,
	VideoPreImage,
}

for RigTemp in NormalRigsterSet:
	admin.site.register(RigTemp)
