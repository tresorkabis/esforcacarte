from django.contrib import admin
from django.urls import path, include

from student.views.home_views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("student/", include('student.urls')),
    path("users/", include('users.urls')),
    path("", HomeView.as_view(), name="home"),
]
