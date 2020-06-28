from urllib import request
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from .forms import UserContact
# Create your views here.
def homepage(request):
    return render(request,'main/index.html')
def mainpage(request):
    return render(request,'main/main.html')
def contact(request):
    form=UserContact()
    return render(request,'main/contact.html',{'form':form})
def webdesign(request):
    return render(request,'main/wb.html')
def graphicsdesign(request):
    return render(request,'main/graphics.html')
def socialmedia(request):
    return render(request,'main/socialmedia.html')
def team(request):
    return render(request,'main/team.html')