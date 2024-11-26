from django.urls import path
from .views import SpyCatDetailView

urlpatterns = [
    path("spycats/", SpyCatDetailView.as_view(), name="spycat-list-create"),
    path("spycats/<int:pk>/", SpyCatDetailView.as_view(), name="spycat-detail"),
]
