import requests
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
def policy(request):
    return render(request,'main/privacyPolicy.html')
def strategy(request):
    return render(request,'main/strategy.html')
def error_404(request,exception):
    return render(request,'main/404.html',status=404)
def error_500(request):
    return render(request,'main/500.html',status=500)
def contactpost(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contact=request.POST['number']
        message=request.POST['message']
        param={
            "firstname":firstname,
            "lastname":lastname,
            "email":email,
            "contact":contact,
            "message":message
        }
        response=requests.post("https://ardmedia.herokuapp.com/contact?api_key=9847c593c7c5a0fb93d08acc913b72eddef37fd594625f6c090bb5af08e33ea8",json=param)
        print(str(response))  #remove in production
        print(firstname)       #remove in production
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/contact')
def landingpost(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        email=request.POST['email']
        param={
            "firstname":firstname,
            "email":email
        }
        response=requests.post("https://ardmedia.herokuapp.com/landing?api_key=9847c593c7c5a0fb93d08acc913b72eddef37fd594625f6c090bb5af08e33ea8",json=param)
        print(str(response))     #remove in production
    return HttpResponseRedirect('/')
def subscribepost(request):
    if request.method=='POST':
        email=request.POST['email']
        param={
            "email":email
        }
        response=requests.post("https://ardmedia.herokuapp.com/subscribe?api_key=9847c593c7c5a0fb93d08acc913b72eddef37fd594625f6c090bb5af08e33ea8",json=param)
        print(str(response))     #remove in production
    return HttpResponseRedirect('/')


    

    

