from django.urls import path
from .views import home_view
from django.contrib.auth import views

app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
]