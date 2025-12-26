from django.urls import path
from . import views

urlpatterns = [
    path("machines/", views.MachineListCreateView.as_view()),
    path("machines/<int:pk>/", views.MachineDetailView.as_view()),
    path("machine-types/", views.MachineTypeListCreateView.as_view()),
    path("machine-types/<int:pk>/", views.MachineTypeDetailView.as_view()),
]