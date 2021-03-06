from typing import Text
from django.shortcuts import redirect, render
import requests
from .models import Comment, question_list
from django.core import serializers
from django.http import HttpResponseRedirect
from .getProfile import get


# Create your views here.
def list(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    questions = question_list.objects.all()
    data = {"questions_list": questions, "check":_context['check']}
    return render(request,'list.html',data)

def add(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True

    if request.method == 'POST':
        if request.POST.get('title') and _context['check'] == True and request.POST.get('nickname') and request.POST.get('text') and request.POST.get('cateogry') and request.POST.get('answer'):
            try:
                post=question_list()
                post.cateogry= request.POST.get('cateogry')
                post.title= request.POST.get('title')
                post.nickname= get(request)["name"]
                post.kakaotalkid= get(request)["id"]
                post.text= request.POST.get('text')
                post.answer= request.POST.get('answer')
                post.save()
            except:
                pass
            return redirect('/comm/')
        else:
            return render(request,'index.html',{"check":_context['check']})
    else:
        return render(request,'index.html',{"check":_context['check']})

def detail(request,question_id):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    questions = serializers.serialize("json", question_list.objects.filter(id=question_id))
    comment = Comment.objects.filter(question_id=question_id)
    data = {"questions": questions, "comment":comment, "check":_context['check']}
    if request.method == 'POST':
        if request.POST.get('text') and request.POST.get('nick') and _context['check'] == True:
            try:
                post=Comment()
                post.nickname= get(request)["name"]
                post.text= request.POST.get('text')
                post.question_id=question_list(id=question_id)
                post.like=0
                post.unlike=0
                post.save()
            except:
                pass
            return render(request,'sub.html',data)

        elif request.POST.get('finger_id') and request.POST.get('finger_text'):
            finger = Comment.objects.get(id=request.POST.get('finger_id'))
            finger.like = int(request.POST.get('finger_text'))+1
            finger.save()
            return render(request,'sub.html',data)

        elif request.POST.get('unfinger_id') and request.POST.get('unfinger_text'):
            finger = Comment.objects.get(id=request.POST.get('unfinger_id'))
            finger.unlike = int(request.POST.get('unfinger_text'))+1
            finger.save()
            return render(request,'sub.html',data)

        elif request.POST.get('cnt'):
            from django.http import HttpResponse
            vote = question_list.objects.get(id=question_id)
            oriText = question_list.objects.get(id=question_id).answer
            tmpList=oriText.split('#')
            count = int(request.POST.get('cnt'))
            tmpList[count]=str(int(tmpList[count])+1)
            vote.answer="#".join(tmpList)
            vote.save()
            return HttpResponse(vote.answer)
        
        elif request.POST.get('del'):
            try:
                kakaomail=get(request)["id"]
                pageinfo = question_list.objects.get(id=question_id).kakaotalkid
                if str(kakaomail) == str(pageinfo):
                    page = question_list.objects.get(id=question_id)
                    page.delete()
                    return HttpResponseRedirect('/comm/')
                else:
                    return HttpResponseRedirect('/comm/'+str(question_id))
            except:
                return HttpResponseRedirect('/comm/'+str(question_id))
        else:
            return render(request,'sub.html',data)

    else:
        return render(request,'sub.html',data)
    
