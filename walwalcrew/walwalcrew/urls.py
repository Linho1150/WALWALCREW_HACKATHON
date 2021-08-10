"""walwalcrew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import question.views
import communication.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/',question.views.question,name='question'),
    path('comm/',communication.views.list,name='communication'),
    path('add/',communication.views.add,name='communication_add'),
    path('comm/<int:question_id>',communication.views.detail,name='comm_detail'),
    path('pass/',accounts.views.question_pass,name='question_pass'),
    path('fail/',accounts.views.fail,name='question_fail'),
    path('', accounts.views.main, name='main'),
    path('kakaoLoginLogic/', accounts.views.kakaoLoginLogic, name='login'),
    path('kakaoLoginLogicRedirect/', accounts.views.kakaoLoginLogicRedirect, name='redirect'),
    path('kakaoLogout/', accounts.views.kakaoLogout, name='logout'),
    path('aboutus/', accounts.views.aboutus, name='aboutus'),
    path('adoption/', accounts.views.adoption, name='adoption')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)