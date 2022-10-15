from django.shortcuts import render
from django.http import HttpResponse
def basehtmlrender(request):
    return render(request,"base.html")

def registration(request):
    return render(request,"register.html")

def Login(request):
    return render(request,"Login.html")

def GetDetailsFromUSer(request):
    return render(request,"SearchBoundaryDetails.html")

def sendDetailsToUser(request):
     return render(request,"DisplayBoundaryDetails.html")
def profile(request):
    return render(request,'profile.html')

