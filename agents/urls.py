from django.urls import path
from .views import get_all_agent_data
from .views import get_agent_status
from .views import get_last_scan
urlpatterns = [
    path('list',get_all_agent_data.get_all_agent),
    path('status',get_agent_status.get_agent_status),
    path('sca-last-scan',get_last_scan.get_last_scan),
]