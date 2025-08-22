from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task

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
            """ For Django Form Data """
            # # print(form.cleaned_data)
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')
            
            # task = Task.objects.create(title=title, description=description, due_date=due_date)
            
            # # assigne employee to tasks
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)
            
            # return HttpResponse("Task Added Successfully")
            
            
            """ For Model Form Data """
            form.save()
            
            return render(request, 'task_form.html', {"form": form, "message": "task added successfully"})
            
    context = {"form": form}
    return render(request, "task_form.html", context)