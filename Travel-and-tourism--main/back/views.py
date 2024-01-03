from django.shortcuts import render, redirect
from .models import *

from .forms import *


# def index(request):
#     return HttpResponse("<h1>This is the first</h1>")
# Create your views here.

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')


def singapore(request):
    return render(request, 'singapore.html')


def about(request):
    return render(request, 'about.html')

def Terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')


def contact(request):
    if request.method == "POST":
        form = insertdata(request.POST)
        if form.is_valid():  # The is_valid() method is used to perform validation for each field of the form, it is defined in Django Form class. It returns True if data is valid and place all data into a cleaned_data attribute.
            f = form.save(commit=False)
            f.save()
        else:
            form.errors
    else:
        form = insertdata()
    return render(request, 'contact.html', {'form': form})


def dubai(request):
    return render(request, 'dubai.html')


def seychelles(request):
    return render(request, 'seychelles.html')


def thailand(request):
    return render(request, 'thailand.html')





########### register here #####################################
def empRegis(request):
    if request.method == "GET":
        form1 = EmpRegisForm()
    if request.method == "POST":
        form1 = EmpRegisForm(request.POST)
        form1.save()
        return redirect('empRegis')

    return render(request, 'login.html', {'form1': form1})


def loginin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        #if form.is_valid():
           # try:
        q = Sign.objects.filter( 
                    email = request.POST['email'],
                    password = request.POST['password'] )
        if len(q)>0:
                    return redirect('home')
           # except:
              #  return redirect('mital:signin')
        else:
                     return redirect('loginin') 
               
    else:
        form = SignInForm()
    return render( request, 'signin.html', {'form':form} )