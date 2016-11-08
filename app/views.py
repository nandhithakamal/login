from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request) :
	return render(request, 'app/homepage.html', {})
	
def Register(request) :
	return render(request, 'app/register.html', {})
	
def Login(request) :
	return render(request, 'app/loginpage.html', {})