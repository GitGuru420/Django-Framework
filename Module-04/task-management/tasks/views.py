from django.shortcuts import render
from django.http import HttpResponse

# app folder templates
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        'names': ['Mahmud', 'Ahmed', 'John'],
        'age': 23
    }
    return render(request, "test.html", context)