from django.shortcuts import render
from .forms import *
# Create your views here.
def home(request):
    form = Form
    mydict={
        'form':form
    }
    return render(request, 'index.html', context=mydict)