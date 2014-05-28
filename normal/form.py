# coding=utf-8 
from django import forms
from django.forms.widgets import *
from backend.utility import validate_fize

class UpLoadPicForm(forms.Form):
    title=forms.CharField(max_length=100,help_text='Your name')
    # pic=forms.FileField(validators=[validate_fize])
    pic=forms.FileField()