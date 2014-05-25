# -*- coding: UTF-8 -*-
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from const import AUTH_CHOICES,VISITOR_USER

class UserIdentity(models.Model):
    """
    Login User identity: AdminStaff, AdminSystem, Expert, SchoolTeam, visitor,
    """
    identity = models.CharField(max_length=50, blank=False, unique=True,
                                choices=AUTH_CHOICES, default=VISITOR_USER,
                                verbose_name="身份级别")
    auth_groups = models.ManyToManyField(User, related_name="identities")

    class Meta:
        verbose_name = u"登录权限"
        verbose_name_plural = u"登录权限"

    def __unicode__(self):
        return self.get_identity_display()