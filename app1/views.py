from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test1(request):
    return HttpResponse("<h1>Hello i am test1</h1>")