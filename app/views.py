from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
# Create your views here.
def Home(request) :
	return render(request, 'app/homepage.html', {})
	
def Register(request) :
	return render(request, 'app/register.html', {})
	
def Login(request) :
	return render(request, 'app/login.html', {})
	
def Redirect(request) :
	return HttpResponseRedirect('app/homepage.html')
	
def Page(request) :
	return render(request, 'app/page.html', {})