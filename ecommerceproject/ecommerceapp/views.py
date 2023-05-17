from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from . import models
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def index(request):
    return render(request,"ecommerceapp/mainscreen.html")


def about(request):
    return render(request,"ecommerceapp/about.html")


def electronic_page(request):
    electronic_items = models.ProductsOnSale.objects.filter(Q(productType="Electronic")).all()
    electronic_items_dict={"electronic_items": electronic_items}
    return render(request,'ecommerceapp/electronic.html', context=electronic_items_dict)









def clothes_page(request):
    clothes_items = models.ProductsOnSale.objects.filter(Q(productType="Clothes")).all()
    clothes_items_dict={"clothes_items": clothes_items}
    return render(request,'ecommerceapp/clothes.html', context=clothes_items_dict)


def home_appliances_page(request):
    home_appliances_items = models.ProductsOnSale.objects.filter(Q(productType="Home Appliances")).all()
    home_appliances_items_dict={"home_appliances_items": home_appliances_items}
    return render(request,'ecommerceapp/homeappliances.html', context=home_appliances_dict)


def cosmetic_page(request):
    cosmetic_items = models.ProductsOnSale.objects.filter(Q(productType="Cosmetic")).all()
    cosmetic_items_dict={"cosmetic_items": cosmetic_items}
    return render(request,'ecommerceapp/cosmetic.html', context=cosmetic_items_dict)

def sport_outdoor_page(request):
    sport_outdoor_items = models.ProductsOnSale.objects.filter(Q(productType="Sport Outdoor")).all()
    sport_outdoor_items_dict={"sport_outdoor_items": sport_outdoor_items}
    return render(request,'ecommerceapp/sportandoutdoor.html', context=sport_outdoor_items_dict)


def car_part_page(request):
    car_part_items = models.ProductsOnSale.objects.filter(Q(productType="Car Part")).all()
    car_part_items_dict={"car_part_items": car_part_items}
    return render(request,'ecommerceapp/carpart.html', context=car_part_items_dict)

def garden_equipment_page(request):
    garden_equipment_items = models.ProductsOnSale.objects.filter(Q(productType="Garden Equipment")).all()
    garden_equipment_items_dict={"garden_equipment_items": garden_equipment_items}
    return render(request,'ecommerceapp/gardenequipment.html', context=garden_equipment_items_dict)






class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"