from django.urls import path
from . import views

app_name = "entry_logs"

urlpatterns = [

    path('logs', views.show_logs, name="logs"),
]
