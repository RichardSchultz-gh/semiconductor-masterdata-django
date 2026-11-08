from django.urls import path
from lots import views

app_name = "lots"

urlpatterns = [
    path("<str:lotid>/edit/", views.lot_edit, name="lot_edit"),
]
