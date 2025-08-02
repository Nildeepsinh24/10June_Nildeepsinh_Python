import random
from django.shortcuts import render

# Create your views here.
def index(request):
    name="Neel"
    return render(request,'index.html',{'name':name})

num = 0
def newpage(request):
    global num
    num+=1
    if num>10:
        num=0
    return render(request,'newpage.html',{'num':num})