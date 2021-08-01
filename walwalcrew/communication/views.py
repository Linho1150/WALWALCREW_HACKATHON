from typing import Text
from django.shortcuts import render
from .models import Comment, question_list
from django.core import serializers

# Create your views here.
def list(request):
    questions = question_list.objects.all()
    data = {"questions_list": questions}
    return render(request,'list.html',data)

def add(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('nickname') and request.POST.get('text') and request.POST.get('cateogry') and request.POST.get('answer'):
            post=question_list()
            post.cateogry= request.POST.get('cateogry')
            post.title= request.POST.get('title')
            post.nickname= request.POST.get('nickname')
            post.text= request.POST.get('text')
            post.answer= request.POST.get('answer')
            post.save()
            return render(request, 'index.html')  
    else:
        return render(request,'index.html')

def detail(request,question_id):
    questions = serializers.serialize("json", question_list.objects.filter(id=question_id))
    comment = Comment.objects.filter(question_id=question_id)
    data = {"questions": questions, "comment":comment}
    return render(request,'sub.html',data)