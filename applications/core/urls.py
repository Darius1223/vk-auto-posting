from django.urls import path

from applications.core import views

urlpatterns = [
    path("callback/", views.callback_view, name="callback"),
]
