from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='color: purple'>Welcome to the Task Management System</h1>")

def contact(request):
    return HttpResponse("<h1 style='color: red'>This is Contact Page</h1>")

def show_task(request):
    return HttpResponse("<h1 style='color: blue'>This is our Task Page</h1>")