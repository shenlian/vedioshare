# Create your views here.
# coding: UTF-8
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.shortcuts import render_to_response,get_object_or_404 ,render

from normal.models import *
from users.models import *
from backend.logging import logger, loginfo

@dajaxice_register
def FileDeleteConsistence(request, nid, fid):
    """
    Delete files in history file list
    """
    logger.info("sep delete files"+"**"*10)
    # check mapping relation
    print "delete"
    f = VideoSubmisson.objects.get(file_id=fid)
    print "haha"
    n = NormalProfile.objects.get(id=nid)

    logger.info(f.normalfile_id.id)
    logger.info(n.id)

    if f.normalfile_id.id != n.id:
        return simplejson.dumps({"is_deleted": False,
                                 "message": "Authority Failed!!!"})

    if request.method == "POST":
        print "delete in"
        f.delete()
        print "delete end"
        return simplejson.dumps({"is_deleted": True,
                                 "message": "delete it successfully!",
                                 "fid": str(fid)})
    else:
        return simplejson.dumps({"is_deleted": False,
                                 "message": "Warning! Only POST accepted!"})
