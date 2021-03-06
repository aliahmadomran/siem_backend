"""siem_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgi import test
from django.contrib import admin

from siem_backend.test import return_token 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', return_token),
    path('agents/',include('agents.urls')),
    path('integrity_monitoring/',include('integrity_monitoring.urls')),
    path('security_events/',include('security_events.urls')),
    path('system_auditing/',include('system_auditing.urls')),
    path('vulnerabilities/',include('vulnerabilities.urls'))
]
