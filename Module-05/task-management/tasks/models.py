from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # many to one
    project = models.ForeignKey(
        'Project', 
        on_delete=models.CASCADE,
        default=1
    )
    
# one to one
class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
    task = models.OneToOneField(
        Task, 
        on_delete=models.CASCADE
    )
    
# many to one
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()