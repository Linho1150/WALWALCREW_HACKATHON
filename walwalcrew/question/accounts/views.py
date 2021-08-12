from django.shortcuts import render, redirect
import requests
import json
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from requests import sessions
from .models import nickname_list



#def main(request):
    #return render(request, 'main.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def adoption(request):
    return render(request, 'adoption.html')
    
def failure(request):
    return render(request, 'failure.html')

def passage(request):
    return render(request, 'passage.html')
# Create your views here.

def main(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'main.html', _context)

def kakaoLoginLogic(request):
    _restApiKey = '37c9aa7740e5099865e96d249270858f' # 입력필요
    _redirectUrl = 'http://walwalcrew/kakaoLoginLogicRedirect/'
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
        nickname.save()
        
    return render(request, 'loginSuccess.html')

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
        return render(request, 'loginoutSuccess.html')
    else:
        return render(request, 'logoutError.html')