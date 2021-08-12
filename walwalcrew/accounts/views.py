from django.shortcuts import render, redirect
import requests
import json
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from requests import sessions
from .models import nickname_list
import cv2
from .getProfile import get
import os
import base64
from .models import authentication
import string 
import random 
from datetime import datetime
from django.shortcuts import get_object_or_404, render

def aboutus(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'aboutus.html', _context)

def adoption(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'adoption.html', _context)

    
def fail(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'failure.html', _context)
    
def main(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'main.html', _context)

def kakaoLoginLogic(request):
    _restApiKey = '37c9aa7740e5099865e96d249270858f' # 입력필요
    _redirectUrl = 'http://walwalcrew.com/kakaoLoginLogicRedirect/'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = '37c9aa7740e5099865e96d249270858f' # 입력필요
    _redirect_uri = 'http://walwalcrew.com/kakaoLoginLogicRedirect/'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    user_profile_info_uri = "https://kapi.kakao.com/v2/user/me?access_token="
    user_profile_info_uri += str(_result['access_token'])
    print(user_profile_info_uri)
    user_profile_info_uri_data = requests.get(user_profile_info_uri)
    user_json_data = user_profile_info_uri_data.json()
    print(user_json_data)
    
    nickname = nickname_list()
    nick_db = nickname_list.objects.all()
    if nickname_list.objects.filter(mail=user_json_data['kakao_account']['email']).exists():
        print("이미 존재")    
    else :
        nickname.name = user_json_data['properties']['nickname']
        nickname.mail = user_json_data['kakao_account']['email']
        nickname.kakaoid = user_json_data['id']
        nickname.save()
        
    return redirect('/')

def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    # _url = 'https://kapi.kakao.com/v1/user/unlink'
    # _header = {
    #   'Authorization': f'bearer {_token}',
    # }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return redirect('/')  
    else:
        return redirect('/')  

def question_pass(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
        kakaoidT=get(request)['id']
        authid = nickname_list.objects.get(kakaoid=kakaoidT)
        authText = authentication.objects.get(authentication_id=authid)
        module_dir = os.path.dirname(__file__)
        text1 = "Dog adoption certificate"
        text2 = str(authText.authentication_date)
        text3 = str(authText.id)
        text4 = str(authText.authentication_email)

        img = cv2.imread(os.path.join(module_dir+'\\templates\\blank.jpg'), cv2.IMREAD_COLOR)

        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 

        textsize1 = cv2.getTextSize(text1, font, 1, 2)[0]
        textsize2 = cv2.getTextSize(text2, font, 1, 2)[0]
        textsize3 = cv2.getTextSize(text3, font, 1, 2)[0]
        textsize4 = cv2.getTextSize(text4, font, 1, 2)[0]

        textX1 = (img.shape[1] - textsize1[0]) / 2
        textX2 = (img.shape[1] - textsize2[0]) / 2
        textX3 = (img.shape[1] - textsize3[0]) / 2
        textX4 = (img.shape[1] - textsize4[0]) / 2

        cv2.putText(img, text1, (int(textX1), int(95) ), font, 1, (0,0,0), 1,cv2.LINE_AA)
        cv2.putText(img, text2, (int(textX2), int(175) ), font, 1, (0,0,0), 1,cv2.LINE_AA)
        cv2.putText(img, text3, (int(textX3), int(255) ), font, 1, (0,0,0), 1,cv2.LINE_AA)
        cv2.putText(img, text4, (int(textX4), int(700) ), font, 1, (0,0,0), 1,cv2.LINE_AA)

        png_img = cv2.imencode('.png', img)
        b64_string = base64.b64encode(png_img[1]).decode('utf-8')
    else:
        _LENGTH = 8
        string_pool = string.digits
        result = "" 
        for i in range(_LENGTH) : 
            result += random.choice(string_pool) 

        module_dir = os.path.dirname(__file__)
        text1 = "Dog adoption certificate"
        text2 = datetime.today().strftime("%Y%m%d")
        text3 = result
        text4 = "WalWal Sailor"

        img = cv2.imread(os.path.join(module_dir+'\\templates\\blank.jpg'), cv2.IMREAD_COLOR)

        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 

        textsize1 = cv2.getTextSize(text1, font, 1, 2)[0]
        textsize2 = cv2.getTextSize(text2, font, 1, 2)[0]
        textsize3 = cv2.getTextSize(text3, font, 1, 2)[0]
        textsize4 = cv2.getTextSize(text4, font, 1, 2)[0]

        textX1 = (img.shape[1] - textsize1[0]) / 2
        textX2 = (img.shape[1] - textsize2[0]) / 2
        textX3 = (img.shape[1] - textsize3[0]) / 2
        textX4 = (img.shape[1] - textsize4[0]) / 2

        cv2.putText(img, text1, (int(textX1), int(95) ), font, 1, (0,0,0), 1,cv2.LINE_AA)
        cv2.putText(img, text2, (int(textX2), int(175) ), font, 1, (0,0,0), 1,cv2.LINE_AA)
        cv2.putText(img, text3, (int(textX3), int(255) ), font, 1, (0,0,0), 1,cv2.LINE_AA)
        cv2.putText(img, text4, (int(textX4), int(700) ), font, 1, (0,0,0), 1,cv2.LINE_AA)

        png_img = cv2.imencode('.png', img)
        b64_string = base64.b64encode(png_img[1]).decode('utf-8')
    return render(request,'pass.html',{'img':b64_string,"check":_context['check']})
        
