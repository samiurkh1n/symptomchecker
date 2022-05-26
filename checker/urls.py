from django.urls import path
from checker import views

urlpatterns = [
    path('', views.home, name='home'),
]