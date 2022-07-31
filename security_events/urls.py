from django.urls import path

from .views import get_alerts
from .views import get_authentication_failure
urlpatterns = [
    path('level-12-alerts',get_alerts.get_alerts),
    path('authentication-failure',get_authentication_failure.get_authentication_failure),

]

