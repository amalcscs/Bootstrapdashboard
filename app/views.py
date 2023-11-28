
from django.http import request
from django.shortcuts import render,redirect


def index_dash(request):
    return render(request,'index_dash.html')

def dashboard(request):
    return render(request,'dashboard.html')

def skydash(request):
    return render(request,'skydash.html')