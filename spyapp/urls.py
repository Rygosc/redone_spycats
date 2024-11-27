from django.urls import path
from .views import SpyCatDetailView, MissionView, TargetsView

urlpatterns = [
    path("spycats/", SpyCatDetailView.as_view(), name="spycat-list-create"),
    path("spycats/<int:pk>/", SpyCatDetailView.as_view(), name="spycat-detail"),
    path("missions/", MissionView.as_view(), name="missions"),
    path("missions/<int:pk>/", MissionView.as_view()),
    path("targets/", TargetsView.as_view(), name="targets"),
    path("targets/<int:pk>/", TargetsView.as_view()),
]
