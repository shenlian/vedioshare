# coding: UTF-8

from settings import STATIC_URL, MEDIA_URL

UNDIFINED = "undifined"

# For UserIdentity Table
ADMINSTAFF_USER = "adminstaff"
VISITOR_USER = "visitor"
NORMAL_USER = "normaluser"

AUTH_CHOICES = (
    (ADMINSTAFF_USER, u"管理员"),
    (NORMAL_USER, u"普通用户"),
    (VISITOR_USER, u"游客"),
)