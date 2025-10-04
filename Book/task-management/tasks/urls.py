from django.urls import path
from tasks.views import about_view, show_task_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('show-task/', show_task_view, name='show-task'),
]
