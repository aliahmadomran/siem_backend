from django.urls import path
from .views import get_all_agent_data

urlpatterns = [
    path('list',get_all_agent_data.get_all_agent)
]