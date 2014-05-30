# Create your views here.
# coding: UTF-8
import os
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
        try:
			currenturl = os.path.dirname(os.path.abspath('__file__'))
			fileurl = str(f.file_obj)
			filepath = currenturl+'/media/'+fileurl
#            if f.video_id_set.all():
#                preimage = f.video_id_set.all()[0]
#                preimageurl = str(preimage.file_obj)
#                preimagepath = currenturl + '/media/' + preimageurl	
#                os.remove(preimagepath)
			preimage = f.videopreimage.file_obj
			print preimage
			preimageurl = str(preimage)
			preimagepath = currenturl + '/media/' + preimageurl
			os.remove(preimagepath)
			os.remove(filepath)
        except Exception,e:
        	print e
		f.delete()
        print "delete end"
        return simplejson.dumps({"is_deleted": True,
                                 "message": "delete it successfully!",
                                 "fid": str(fid)})
    else:
        return simplejson.dumps({"is_deleted": False,
                                 "message": "Warning! Only POST accepted!"})
