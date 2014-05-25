# coding: UTF-8
from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

from const.models import *
from const import  ADMINSTAFF_USER, VISITOR_USER, NORMAL_USER

class NormalProfile(models.Model):
    """
    User Profile Extend
    The Administrator can modified them in admin.page
    """
    telephone = models.CharField(max_length=100, blank=True, verbose_name="电话")
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")

    class Meta:
        verbose_name = "普通用户"
        verbose_name_plural = "普通用户"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(NormalProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=NORMAL_USER)
        self.userid.identities.add(auth)


class AdminStaffProfile(models.Model):
    userid = models.ForeignKey(User, unique=True,
                               verbose_name="权限对应ID")
    jobs = models.CharField(max_length=50, blank=True, verbose_name="职务")

    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = "管理员"

    def __unicode__(self):
        return '%s' % (self.userid)

    def save(self, *args, **kwargs):
        super(AdminStaffProfile, self).save()
        auth, created = UserIdentity.objects.get_or_create(identity=ADMINSTAFF_USER)
        self.userid.identities.add(auth)