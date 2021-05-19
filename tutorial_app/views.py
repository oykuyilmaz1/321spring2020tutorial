from django.shortcuts import render, redirect
from django.http import HttpResponse
from tutorial_app.users.login import *
from tutorial_app.users.forms import *

# Create your views here.

def index(request):
    index_text = "view.index is called"
    context = {'index_text': index_text}
    return render(request, 'renders/index.html', context)

def printNumber(request, number):
    numbers = [i for i in range(number, number+5)]
    arr = []
    for i in range(len(numbers)):
        arr.append({"index":i, "number":numbers[i]})
    return render(request, 'renders/numbers.html', {"arr":arr})

def printString(request, string):
    t = string + "321"
    return HttpResponse(f'view.printString function is called with string given: {string} and added \"321\" is: {t}')

def loginIndex(request):
    context = {"login_fail": False, "login_form":LoginForm()}    
    return render(request, 'tutorial_app/login.html', context)

def login(request):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    loginCheck = checkCreditentials(name, surname)
    if(loginCheck):
        request.session['name'] = name
        return redirect('../home')
    context = {"login_fail": True, "login_form":LoginForm()}    
    return render(request, 'tutorial_app/login.html', context)

def home(request):
    name = request.session['name']
    return render(request, 'tutorial_app/home.html', {"name":name})