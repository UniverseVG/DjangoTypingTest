from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from App.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from App.models import Previous_Score




#-------------Landing Page-------------------
def LandingPage(request):
    return render(request,'LandingPage.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')

#------------Register Page-------------------
def register(request):
    #if user is logged in,it should not access register page,it should send 'index' page
    if request.user.is_authenticated:
        return redirect('dashboard')
    #if user is not logged in,it should access register page,    
    else:    
        if request.method == "POST":
            form = RegisterForm(request.POST)
            #validating the form
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request,'register.html',{'form' :form})

#-------------Logic Page-------------------
@login_required
def Dashboard(request):
    return render(request,'dashboard.html')

def index(request):
    return render(request,'index.html')


def index2(request):
    return render(request,'index2.html')
   

#--------------Performance----------------
@csrf_exempt
def Save_To_Database(request):
    if request.method == 'GET':
        print("yes")
        wpm       =   int(request.GET['wpm'])
        cpm       =   int(request.GET['cpm'])
        errors    =   int(request.GET['errors'])
        accuracy  =   int(request.GET['acc'])
        Time      =   120
        obj       =   Previous_Score(manager=request.user,W_pm=wpm,C_pm=cpm,Errors=errors,Accuracy=accuracy,Time=Time)
        obj.save()    
    return HttpResponse()

#-------------Previous Score -----------------
@login_required
def Performance(request):
    Scores         = Previous_Score.objects.filter(manager=request.user)
    return render(request,'Performance.html',{'Score' : Scores})
