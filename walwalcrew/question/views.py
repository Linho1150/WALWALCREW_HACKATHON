from django.http import request
from django.shortcuts import render
from .models import question as question_model
from django.core import serializers
import cv2
import base64
import os

# Create your views here.
def question(request):
    #questions =  question_model.objects.values()
    questions = serializers.serialize("json", question_model.objects.all())
    data = {"questions": questions}
    return render(request,'question.html',data)

def question_fail(request):
    return render(request,'fail.html');

def question_pass(request,passnum):
    module_dir = os.path.dirname(__file__)
    text1 = "walwal"
    text2 = "20210806"
    text3 = "1234"
    text4 = "walwalcrew"

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
    return render(request,'pass.html',{'img':b64_string})
