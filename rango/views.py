from django.shortcuts import render
from django.http import HttpResponse
#Each view exists as a series of individual functions, in this instance called index
def index(request):
    #Importing the HttpResponse object from the django.http module
    return HttpResponse("It workssss!")
