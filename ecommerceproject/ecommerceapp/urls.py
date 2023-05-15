
from django.urls import path
from . import views

app_name = "ecommerceapp"

urlpatterns = [
    path("",views.index,name="index"),
]