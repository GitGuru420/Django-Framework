from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg

# app folder templates
def manager_dashboard(request):
    tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()
    
    # getting task count
    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status="COMPLETED").count()
    # in_progress_task = Task.objects.filter(status="IN_PROGRESS").count()
    # pending_task = Task.objects.filter(status="PENDING").count()

    # count = {
    #     "total_task": total_task,
    #     "completed_task": completed_task,
    #     "in_progress_task": in_progress_task,
    #     "pending_task": pending_task
    # }
    
    counts = Task.objects.aggregate(
        total = Count('id'),
        completed = Count('id', filter=Q(status="COMPLETED")),
        in_progress = Count('id', filter=Q(status="IN_PROGRESS")),
        pending = Count('id', filter=Q(status="PENDING"))
    )
    
    context = {
        "tasks": tasks,
        "counts": counts
    }
    return render(request, "dashboard/manager-dashboard.html", context)

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
    # task_count = Task.objects.aggregate(num_task=Count('id'))
    
    # projects = Project.objects.annotate(num_task=Count('task'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})