# Generated by Django 4.1 on 2023-05-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0003_alter_productsonsale_productprice"),
    ]

    operations = [
        migrations.CreateModel(
            name="Buyitem",
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
                ("item_pk", models.IntegerField(max_length=100)),
                ("who_buy", models.CharField(max_length=50)),
            ],
        ),
    ]
