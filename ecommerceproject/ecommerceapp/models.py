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


