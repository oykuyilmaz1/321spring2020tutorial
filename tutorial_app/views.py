from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("view.index function is called")

def printNumber(request, number):
    t = number + 5
    return HttpResponse(f'view.printNumber function is called with number given: {number}, and 5 more of it is: {t}')

def printString(request, string):
    t = string + "321"
    return HttpResponse(f'view.printString function is called with string given: {string} and added \"321\" is: {t}')