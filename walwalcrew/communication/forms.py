from django import forms
from .models import question_list

class addFrom(forms.ModelForm):
    class Meta:
        model= question_list
        fields= ["id","cateogry", "title", "text", "answer"]