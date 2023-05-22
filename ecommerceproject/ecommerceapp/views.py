from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
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
    return render(request,'ecommerceapp/homeappliances.html', context=home_appliances_items_dict)


def cosmetic_page(request):
    cosmetic_items = models.ProductsOnSale.objects.filter(Q(productType="Cosmetic")).all()
    cosmetic_items_dict={"cosmetic_items": cosmetic_items}
    return render(request,'ecommerceapp/cosmetic.html', context=cosmetic_items_dict)

def sport_outdoor_page(request):
    sport_outdoor_items = models.ProductsOnSale.objects.filter(Q(productType="Sport Outdoor")).all()
    sport_outdoor_items_dict={"sport_outdoor_items": sport_outdoor_items}
    return render(request,'ecommerceapp/sportandoutdoor.html', context=sport_outdoor_items_dict)


def car_part_page(request):
    car_part_items = models.ProductsOnSale.objects.filter(Q(productType="Car Parts")).all()
    car_part_items_dict={"car_part_items": car_part_items}
    return render(request,'ecommerceapp/carpart.html', context=car_part_items_dict)

def garden_equipment_page(request):
    garden_equipment_items = models.ProductsOnSale.objects.filter(Q(productType="Gardan Equipment")).all()
    garden_equipment_items_dict={"garden_equipment_items": garden_equipment_items}
    return render(request,'ecommerceapp/gardenequipment.html', context=garden_equipment_items_dict)

def detail(request,pk):
    detail = models.ProductsOnSale.objects.get(pk=pk)
    detail_dict = {"detail": detail}
    return render(request, 'ecommerceapp/detail.html',context=detail_dict)


@login_required(login_url="/login")
def addbuyitem(request,pk):
    if request.POST:
        print("denee")
    else:
        models.Buyitem.objects.create(item_pk=pk,who_buy = request.user)
        return redirect('ecommerceapp:index')
   
@login_required    
def cart(request):
    username= request.user
    items = models.Buyitem.objects.filter(Q(who_buy=username)).all()
    sonra = len(items)
    item_list=[]
    total_price= 0
    for i in range(sonra) :
        item_pk = items[i].item_pk
        item = models.ProductsOnSale.objects.get(pk=item_pk)
        item_price = item.productPrice
        total_price = total_price + item_price
        item_list.append(item)

    denemeler = total_price*0.18   
    tax = float("%.2f" % denemeler)
    row_price_calculation = total_price-tax
    row_price = float("%.2f" %  row_price_calculation)
    context={"item_list":item_list, "total_price": total_price , "tax": tax , "row_price": row_price }    
    return render(request,"ecommerceapp/cart.html", context=context)

@login_required
def deletecart(request,pk):
    models.Buyitem.objects.filter(who_buy=request.user,item_pk = pk)[0].delete()
    return redirect("ecommerceapp:cart")


@login_required(login_url="/login")
def payment (request):
    username= request.user
    items = models.Buyitem.objects.filter(Q(who_buy=username)).all()
    sonra = len(items)
    item_list=[]
    total_price= 0
    for i in range(sonra) :
        item_pk = items[i].item_pk
        item = models.ProductsOnSale.objects.get(pk=item_pk)
        item_price = item.productPrice
        total_price = total_price + item_price
        item_list.append(item)
    return render(request,"ecommerceapp/payment.html", context={"item_list": item_list,"total_price": total_price })



@login_required(login_url="/login")
def order (request):
    if request.POST:
        data= request.POST
        print(request.user)
        print(data['username'])
        if str(request.user) == str(data['username']):
            firstName= data['firstName']
            lastName= data['lastName']
            username= data['username']
            email= data['email']
            address1= data['address1']
            address2= data['address2']
            country= data['country']
            state= data['state']
            zip= data['zip']
            paymentMethod= data['paymentMethod']
            ccname= data['ccname']
            ccnumber= data['ccnumber']
            ccexpiration= data['ccexpiration']
            cccvv= data['cccvv']

            username= request.user
            items = models.Buyitem.objects.filter(Q(who_buy=username)).all()
            sonra = len(items)
            item_pk_list=[]
            total_price= 0
            for i in range(sonra) :
                item_pk = items[i].item_pk
                item = models.ProductsOnSale.objects.get(pk=item_pk)
                item_price = item.productPrice
                total_price = total_price + item_price
                item_pk_list.append(item_pk)
            

            models.OrderForm.objects.create(first_name=firstName,
                                            Last_name=lastName,
                                            username=username,
                                            email=email,
                                            address1=address1,
                                            address2=address2,
                                            country=country,
                                            state=state,
                                            zip=zip,
                                            payment=paymentMethod,
                                            name_on_card=ccname,
                                            credit_card_number=ccnumber,
                                            expiration=ccexpiration,
                                            CVV=cccvv,
                                            price= total_price,
                                            ordered_items_pk=str(item_pk_list))
            for i in item_pk_list:
                models.Buyitem.objects.filter(who_buy=username,item_pk = i).delete()
            

            return redirect("ecommerceapp:cart")
        else:
            print("sorun")
            pass
    else:
        pass    


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"




