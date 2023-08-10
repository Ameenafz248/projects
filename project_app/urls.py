from django.urls import path
from .views import ListProject, IncreaseHitView

urlpatterns = [
    path("<uuid:project_id>", IncreaseHitView.as_view(), name="increase_hits"),
    path("", ListProject.as_view(), name="project_list"),
]