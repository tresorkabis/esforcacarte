from django.urls import path

from users.views import RequestAccount


urlpatterns = [
    path("request-account/", RequestAccount.as_view(), name="request_account"),
]