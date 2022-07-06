from django.urls import path
from .views import get_all_agent_data,get_agent_status

urlpatterns = [
    path('list',get_all_agent_data.get_all_agent),
    path('status',get_agent_status.get_agent_status)
]