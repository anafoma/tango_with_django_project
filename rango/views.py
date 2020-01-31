from django.shortcuts import render
from django.http import HttpResponse
#Each view exists as a series of individual functions, in this instance called index
def index(request):
    #Importing the HttpResponse object from the django.http module
   context_dict={'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
   return render(request, 'rango/index.html', context=context_dict)
#view method called about 
def about(request):
    context_dict={'boldmessage':'This tutorial has been put up together by Ana'}
    return render(request,'/rango/about.html', context=context_dict)

