from django.shortcuts import render,redirect
from data.models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from data.forms import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(r):
    context = {
        'cat':Category.objects.all(),
        'hed':Headline.objects.all(),
    }
    return render(r,'home.html',context)

def cat(r,cat_slug):
    context= {
        'hed':Headline.objects.filter(category__slug=cat_slug),
        'cat':Category.objects.all(),
    }
    return render(r,'home.html',context)

@login_required(login_url='login')
def registers(r):
    if r.user.is_authenticated:
        return redirect('adminpage')
    else:
        form = CreateuserForm()
        if r.method == 'POST':
            form = CreateuserForm(r.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
                
        context = {
            'form':form,
        }
        return render(r,'signup.html',context)

def logins(r):
    if r.user.is_authenticated:
        return redirect('homepage')
    else:
        if r.method == 'POST':
            username = r.POST.get('username')
            password = r.POST.get('password')

            user = authenticate(r, username=username, password=password)

            if user is not None:
                login(r, user)
                return redirect('adminpage')
            else:
                return redirect('login')

    return render(r,'login.html')

@login_required(login_url='login')
def logoutad(r):
    logout(r)
    return redirect('login')

@login_required(login_url='login')
def catadd(r):
    form = Addcat(r.POST or None)
    if r.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(adminPage)
    context = {
        'form':form,
    }
    return render(r,'catadd.html',context)

@login_required(login_url='login')
def headadd(r):
    form = Addheadline(r.POST or None , r.FILES or None)
    if r.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(adminPage)
    context = {
        'form':form,
    }
    return render(r,'headadd.html',context)

@login_required(login_url='login')
def viewcat(r):
    context = {
        'cat':Category.objects.all(),
    }
    return render(r,'viewcat.html',context)

@login_required(login_url='login')
def viewhead(r):
    context = {
        'head':Headline.objects.all(),
    }
    return render(r,'viewhed.html',context)

    
@login_required(login_url='login')
def adminPage(r):
    return render(r,'admin.html')


