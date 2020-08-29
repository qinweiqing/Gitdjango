from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("login")
def reg(request):
    return HttpResponse("reg")
def reg2(request):
    return HttpResponse("reg2")