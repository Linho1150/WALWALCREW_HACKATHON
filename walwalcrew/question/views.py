from django.shortcuts import render
from .models import question as question_model
from django.core import serializers

# Create your views here.
def question(request):
    #questions =  question_model.objects.values()
    questions = serializers.serialize("json", question_model.objects.all())
    data = {"questions": questions}
    return render(request,'question.html',data)
