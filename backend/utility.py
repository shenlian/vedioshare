# coding: UTF-8
from django.core.exceptions import ValidationError

def validate_fize(value):
    print str(value.size) 
    if value.size < 6*1024*1024:
        raise ValidationError(u'sorry ,the size is too large',code='_invalid') 

def handle_uploaded_file(f):
    destination = open('some/file/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()