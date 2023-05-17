# Generated by Django 4.1 on 2023-05-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductsOnSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("companyname", models.CharField(max_length=50)),
                ("productType", models.CharField(max_length=30)),
                ("productName", models.CharField(max_length=100)),
                ("productPrice", models.PositiveIntegerField()),
                ("productdescription", models.CharField(max_length=200)),
                ("creationDate", models.DateTimeField(auto_now_add=True)),
                ("product_image", models.FileField(blank=True, upload_to="")),
            ],
        ),
    ]
