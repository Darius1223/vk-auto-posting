from django.urls import path

from apps.core import views

urlpatterns = [
    path("callback/", views.callback_view, name="callback"),
]
