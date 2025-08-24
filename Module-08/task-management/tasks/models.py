from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', ('Pending')),
        ('IN_PROGRESS', ('In Progress')),
        ('COMPLETED', ('Completed'))
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # many to one
    project = models.ForeignKey(
        'Project', 
        on_delete=models.CASCADE,
        default=1
    )
    
    # many to many
    assigned_to = models.ManyToManyField(
        'Employee',
        related_name='tasks'
    )
    
    def __str__(self):
        return self.title
    
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
    # assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
    task = models.OneToOneField(
        Task, 
        on_delete=models.CASCADE,
        related_name='details'
    )
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Details for task {self.task.title}"
    
# many to one
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
# many to many
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name