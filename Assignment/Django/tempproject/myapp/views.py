from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def shop(request):
    return render(request,'shop.html')
def single(request):
    return render(request,'single.html')
def contact(request):
    return render(request,'contact.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')
def bestseller(request):
    return render(request,'bestseller.html')
def error(request):
    return render(request,'404.html')
