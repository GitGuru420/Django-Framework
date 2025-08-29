from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Task Management System</h1>")

def contact(request):
    return HttpResponse("<h1>This is our Contact Page</h1>")