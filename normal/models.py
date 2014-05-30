# coding: UTF-8

import uuid
import os
import datetime
from django.db import models
from users.models import NormalProfile
# Create your models here.

class VideoSubmisson(models.Model):
    file_id = models.CharField(max_length=50,
                               primary_key=True, default=lambda:str(uuid.uuid4()),
                               verbose_name="文件上传唯一ID")
    normalfile_id = models.ForeignKey(NormalProfile)
    name = models.CharField(max_length=100, blank=False,
                            verbose_name="文件名称")
    file_obj = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/%m-%Y'),
                                verbose_name="文件对象")
    uploadtime = models.DateTimeField(blank=True, null=True,
                                      verbose_name="上传时间")
    file_size = models.CharField(max_length=50, blank=True, null=True,
                                 default=None, verbose_name="文件大小")
    file_type = models.CharField(max_length=50, blank=True, null=True,
                                 default=None, verbose_name="文件类型")

    class Meta:
        verbose_name = "文件上传"
        verbose_name_plural = "文件上传"

    def __unicode__(self):
        return self.normalfile_id.userid
    def file_name(self):
        return os.path.basename(self.file_obj.name)

class VideoPreImage(models.Model):
    file_id = models.CharField(max_length=50,
                               primary_key=True, default=lambda:str(uuid.uuid4()),
                               verbose_name="文件上传唯一ID")
    video_id = models.OneToOneField(VideoSubmisson)
    file_obj = models.FileField(upload_to=datetime.datetime.now().strftime('uploadfile/preimage/%m-%Y'),
                                verbose_name="文件对象")
    uploadtime = models.DateTimeField(blank=True, null=True,
                                      verbose_name="上传时间")
   
