from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def foo(request):
	return HttpResponse("<a href='HelloWorldApp'>Hello World!</a>")

def bar(request):
	return HttpResponse("<h1 style='color:red'>You are a faggot!</h1>")
