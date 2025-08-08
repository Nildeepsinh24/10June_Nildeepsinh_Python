from django.shortcuts import render
#pass neel2405
#user neeldeepsinh
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
