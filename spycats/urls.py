# project_name/urls.py (where settings.py is located)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("spyapp.urls")),
]
