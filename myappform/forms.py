
from tkinter import Widget
from django.forms import ModelForm
from .models import *
from django import forms





class Form(forms.ModelForm):
    class Meta: 
        model = Date
        fields = "__all__"
        Widgets={
            'firstdate':forms.TextInput(attrs={'class':'form-control'}),
            'seconddate':forms.NumberInput(attrs={'class':'form-control'}),
        }