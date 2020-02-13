from django.shortcuts import render
from django.http import HttpResponse
#Each view exists as a series of individual functions, in this instance called index
def index(request):
    #Importing the HttpResponse object from the django.http module
   
    return HttpResponse('Rango says hey there partner! <a href="/rango/about/">About</a>')

#view method called about 
def about(request):

    return HttpResponse('Rango says here is the about page. <a href="/rango/">Index</a>')