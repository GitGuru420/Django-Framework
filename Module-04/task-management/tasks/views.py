from django.shortcuts import render
from django.http import HttpResponse

# root folder templates
def home(request):
    return render(request, "home.html")

def contact(request):
    return HttpResponse("<h1 style='color: red'>This is Contact Page</h1>")

def show_task(request):
    return HttpResponse("<h1 style='color: blue'>This is our Task Page</h1>")
