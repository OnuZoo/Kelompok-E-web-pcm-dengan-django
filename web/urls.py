from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.beranda, name="beranda"),
    path("agenda/", views.agenda, name="agenda"),
]