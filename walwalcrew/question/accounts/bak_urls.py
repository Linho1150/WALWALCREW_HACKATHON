from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('kakaoLoginLogic/', views.kakaoLoginLogic, name='login'),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name='redirect'),
    path('kakaoLogout/', views.kakaoLogout, name='logout'),
    #path('main/', views.main, name='main'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('adoption/', views.adoption, name='adoption'),
    path('failure/', views.failure, name='failure'),
    path('passage/', views.passage, name='passage'),
]
