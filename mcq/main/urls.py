from django.urls import path

from mcq.main import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
]
