from accounts.models import nickname_list
from accounts.models import authentication
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import question as question_model
from django.core import serializers
from django.shortcuts import get_object_or_404, render
import requests
import cv2
import base64
from .getProfile import get

# Create your views here.
def question(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    if request.method == 'POST':
        if request.POST.get('pass'):
            try:
                auth_text=get(request)
                auth_id=get_object_or_404(nickname_list, kakaoid=auth_text['id']).id
                auth=authentication()
                auth.authentication_id=nickname_list(id=auth_id)
                auth.authentication_email=auth_text['email']
                auth.save()
            except:
                pass
            return HttpResponse('/pass')
    questions = serializers.serialize("json", question_model.objects.all())
    data = {"questions": questions, "check":_context['check']}
    return render(request,'question.html',data)

def question_fail(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request,'failure.html',{"check":_context['check']})

