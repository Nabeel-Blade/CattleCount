from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from cattlecount.models import Shed, Employee, Cattle, Lot, MedRec
# Create your views here.


def home(request):
    if request.user.is_superuser:
        data='3'
        return render(request, 'home.html',{'data':data})

    elif request.user.is_authenticated:
        data = request.user.userprofile.get().user_type
        return render(request, 'home.html',{'data':data})

    else:
        return render(request, 'home.html')


def about(request):
    return redirect("/home")

def handledeletecattle(request):
    if request.method == 'POST':
        # Get the Post Parameters
        id = request.POST['id']
        Cattle.objects.filter(id__exact=id).delete()
        return redirect("/home")

def handledeleteemployee(request):
    if request.method == 'POST':
        # Get the Post Parameters
        id = request.POST['id']
        Employee.objects.filter(id__exact=id).delete()
        return redirect("/home")

def handledeleteshed(request):
    if request.method == 'POST':
        # Get the Post Parameters
        id = request.POST['id']
        Shed.objects.filter(id__exact=id).delete()
        return redirect("/home")

def handleaddcattle(request):
    if request.method == 'POST':
        # Get the Post Parameters
        ctype = request.POST['ctype']
        gender = request.POST['gender']
        age = request.POST['age']
        date_acq = request.POST['date_acq']
        buy_cost = request.POST['buy_cost']
        sale_price = request.POST['sale_price']
    
        mycattle = Cattle.objects.create()
        mycattle.ctype = ctype
        mycattle.gender = gender
        mycattle.age = age
        mycattle.date_acq = date_acq
        mycattle.buy_cost = buy_cost
        mycattle.sale_price = sale_price
        mycattle.save()

        messages.success(request, 'Cattle successfully updated!')
        return redirect("/home")
    else:
        return HttpResponse('404 - Not Found!')

def handleaddemployee(request):
    if request.method == 'POST':
        # Get the Post Parameters
        ename = request.POST['ename']
        salary = request.POST['salary']
        jdate = request.POST['jdate']
        jdes = request.POST['jdes']
        
        myemployee = Employee.objects.create()
        myemployee.ename = ename
        myemployee.salary = salary
        myemployee.jdate = jdate
        myemployee.jdes = jdes
        
        myemployee.save()

        messages.success(request, 'Employee successfully updated!')
        return redirect("/home")
    else:
        return HttpResponse('404 - Not Found!')

def handleaddshed(request):
    if request.method == 'POST':
        # Get the Post Parameters
        sname = request.POST['sname']
        
        myshed= Shed.objects.create()
        myshed.sname = sname
        myshed.save()

        messages.success(request, 'Employee successfully updated!')
        return redirect("/home")
    else:
        return HttpResponse('404 - Not Found!')

def viewcattle(request):
        data = Cattle.objects.all
        return render(request,'vcat.html', {'data': data})

def viewemployee(request):
        data = Employee.objects.all
        return render(request,'vemp.html', {'data': data})

def viewshed(request):
        data = Shed.objects.all
        return render(request,'vshed.html', {'data': data})







