from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail
from datetime import date

# app folder templates
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    names = ['Mahmud', 'Ahmed', 'John']
    count = 0
    for name in names:
        count += 1
    context = {
        'names': ['Mahmud', 'Ahmed', 'John'],
        'age': 23,
        'count': count
    }
    return render(request, "test.html", context)

# form : post
def create_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm()    # For GET
    
    # For POST
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        # print(form)
        if form.is_valid():
            
            """ For Model Form Data """
            form.save()
            
            return render(request, 'task_form.html', {"form": form, "message": "task added successfully"})
            
    context = {"form": form}
    return render(request, "task_form.html", context)


def view_task(request):
    # show the that are pending
    # tasks = Task.objects.filter(status="PENDING")
    
    # show the task whcih due date is today
    # tasks = Task.objects.filter(due_date=date.today())
    
    """ show the task whose priority is not low """
    tasks = TaskDetail.objects.exclude(priority="L")
    return render(request, "show_task.html", {"tasks": tasks})