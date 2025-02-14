# myapp/urls.py
from django.urls import path
from . import views  # This imports the views from views.py

urlpatterns = [
    path('', views.index, name='index'),  # This will map the root URL to the 'index' view
]
