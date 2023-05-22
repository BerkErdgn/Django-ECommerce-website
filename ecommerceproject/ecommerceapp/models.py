from django.db import models

# Create your models here.

class ProductsOnSale(models.Model):
    companyname = models.CharField(max_length=50)
    productType = models.CharField(max_length=30)
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productdescription = models.CharField(max_length=800)
    creationDate = models.DateTimeField(auto_now_add= True)
    product_image = models.FileField(blank=True)

    def __str__(self):
        return f"{self.companyname} --> {self.productName} "


class Buyitem(models.Model):
    item_pk = models.IntegerField()
    who_buy = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.who_buy} --> {self.item_pk} "
    
class OrderForm(models.Model):
    first_name= models.CharField(max_length=50)
    Last_name= models.CharField(max_length=50)
    username= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    address1= models.CharField(max_length=50)
    address2= models.CharField(max_length=50, null=True)
    country= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    zip= models.CharField(max_length=50)
    payment= models.CharField(max_length=50)
    name_on_card= models.CharField(max_length=50)
    credit_card_number= models.CharField(max_length=50)
    expiration= models.CharField(max_length=50)
    CVV= models.CharField(max_length=50)
    price= models.CharField(max_length=50)
    ordered_items_pk= models.CharField(max_length=400)

    def __str__(self):
        return f"{self.email} --> {self.price} $ --> {self.username} "

