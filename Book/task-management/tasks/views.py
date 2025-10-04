from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home_view(request):
    return HttpResponse("Welcome to the Task Management System")

# Contact View
def contact_view(request):
    return HttpResponse("This is the contact page. Reach us at contact@taskmanagement.com")

# About View
def about_view(request):
    return HttpResponse("About Us: This is the Task Management System where you can manage your tasks effectively")

# Show Task View
def show_task_view(request):
    return HttpResponse("Show Task: This displays task details and related information")