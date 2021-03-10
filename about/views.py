from django.shortcuts import render, redirect, reverse
from django.conf import settings


def about(request):
    return render(request, 'about/about.html')
