
from django.urls import path
from . import views

app_name = "ecommerceapp"

urlpatterns = [
    path('',views.index,name="index"),
    path('about/', views.about, name="about"),
    path('signup/',views.SignUpView.as_view(), name="signup"),
    path('electronic/', views.electronic_page, name="electronic"),
    path('clothes/', views.clothes_page, name="clothes"),
    path('homeappliances/', views.home_appliances_page, name="homeappliances"),
    path('cosmetic/', views.cosmetic_page, name="cosmetic"),
    path('sportandoutdoor/', views.sport_outdoor_page, name="sportandoutdoor"),
    path('carpart/', views.car_part_page, name="carpart"),
    path('gardenequipment/', views.garden_equipment_page, name="gardenequipment"),
    path('detail/<int:pk>', views.detail,name="detail"),
    path('addbuyitem/<int:pk>', views.addbuyitem, name="addbuyitem"),
    path('cart/',views.cart,name="cart"),
    path('deletecart/<int:pk>', views.deletecart, name="deletecart"),
    path('payment/', views.payment, name="payment"),
    path('order/', views.order, name="order"),
]