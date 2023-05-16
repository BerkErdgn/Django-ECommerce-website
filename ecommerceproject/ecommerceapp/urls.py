
from django.urls import path
from . import views

app_name = "ecommerceapp"

urlpatterns = [
    path('',views.index,name="index"),
    path('about/', views.about, name="about"),
    path('signup/',views.SignUpView.as_view(), name="signup")
]