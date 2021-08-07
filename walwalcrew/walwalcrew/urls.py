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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',question.views.question,name='question'),
    path('comm/',communication.views.list,name='communication'),
    path('comm_add/',communication.views.add,name='communication_add'),
    path('comm/<int:question_id>',communication.views.detail,name='comm_detail'),
    path('pass/<int:passnum>',question.views.question_pass,name='question_pass'),
    path('fail',question.views.question_fail,name='question_fail')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)