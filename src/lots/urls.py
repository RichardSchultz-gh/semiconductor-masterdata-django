from django.urls import path
from lots import views

app_name = "lots"

urlpatterns = [
    path("", views.lot_list, name="lot_list"),
    path("<str:lotid>/edit/", views.lot_edit, name="lot_edit"),
]
