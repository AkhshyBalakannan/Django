from django import forms
from django.db.models import fields
from .models import Question


class To_create_form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_weight', 'question_text']
