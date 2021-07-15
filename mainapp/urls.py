from django.urls import include, path
from .views import UserProfileListCreateView, UserProfileDetailView, RecordView, ExportView, ConfigureView
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    # gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path("records/", RecordView.as_view(), name='record'),
    path("records/export/", ExportView.as_view(), name='export'),
    path("templates/configure/", ConfigureView.as_view(), name='configure'),
]
