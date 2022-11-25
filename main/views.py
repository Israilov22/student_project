from django.shortcuts import render


def index(request):
    return render(request,'main/1/index.html')


def page2(request):
    return render(request,'main/2/page2.html')

def avtorization(request):
    return render(request,'main/3/avtorization.html')

def registr(request):
    return render(request,'main/4/registr.html')