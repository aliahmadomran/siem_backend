from django.urls import path

from .views import get_alerts_view

urlpatterns = [
    path('level-12-alerts',get_alerts_view.get_alerts),
]