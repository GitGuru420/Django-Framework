from django.contrib import admin
from django.urls import path
from tasks.views import home_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
]
