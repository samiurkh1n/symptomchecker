"""symptomchecker URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

import checker

urlpatterns = [
    path('', include('checker.urls')),
    path('admin/', admin.site.urls),
]
