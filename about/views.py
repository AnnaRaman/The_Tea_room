from django.shortcuts import render, redirect, reverse
from django.conf import settings
# Create your views here.


#def about(request):

 #   template = 'about/about.html'

 #   return render(request, template)

def about(request):
    return render(request, 'about/about.html')
