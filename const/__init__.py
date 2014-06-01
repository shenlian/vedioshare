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

# For ContentType Table
CONTENTTYPE_MUSIC  = "music"
CONTENTTYPE_GAME  = "game"
CONTENTTYPE_MOVIE  = "movie"
CONTENTTYPE_TV  = "tv"

CONTENTTYPE_CHOICES = (
    (CONTENTTYPE_MUSIC, u"音乐"),
    (CONTENTTYPE_GAME, u"游戏"),
    (CONTENTTYPE_MOVIE, u"电影"),
    (CONTENTTYPE_TV, u"电视"),
)

