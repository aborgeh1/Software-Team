from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return HttpResponse('registration')

def Login(request):
    return HttpResponse('Login')

def getDetails(request):
    return HttpResponse('getdetails')


def sendDetails(request):
     return HttpResponse('senddetails')

