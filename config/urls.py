from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from student.views.home_views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("student/", include('student.urls')),
    path("users/", include('users.urls')),
    path("", HomeView.as_view(), name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)