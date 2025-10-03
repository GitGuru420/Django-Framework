from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Task Management System project</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to the Task Management System Contact Page</h1>")

def show_task(request):
    return HttpResponse("<h1>This is our Task Page</h1>")