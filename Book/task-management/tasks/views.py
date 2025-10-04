from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home_view(request):
    return HttpResponse("Welcome to the Task Management System")

# Contact View
def contact_view(request):
    return HttpResponse("This is the contact page. Reach us at contact@taskmanagement.com")