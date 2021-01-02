from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120,null=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.IntegerField()
    CATEGOTY  = (
        ('shoes','Shoes'),
        ('watch','Watch'),
        ('tshirt','T-shirt'),
        ('jeans','Jeans'),
    )
    category = models.CharField(max_length=6,choices=CATEGOTY,null=True)
    feachered = models.BooleanField(blank=True,null=True)
    digital = models.BooleanField(blank=True,null=True)
    image = models.ImageField(upload_to='product-images',blank=True,null=True)

    def __str__(self):
        return self.name + " " + self.category
    
    @property
    def ImageUrl(self):
        if self.image.url:
            return self.image.url
        return ''

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    completed = models.BooleanField(default=False,blank=True)
    needshipping = models.BooleanField(default=False,blank=True)
    dateoforder = models.DateTimeField(auto_now_add=True,null=True)

    @property
    def get_total_order_price(self):
        cart = self.cart_set.all()
        sum = 0
        for i in cart:
            sum += i.get_per_product_total
        return sum

    def __str__(self):
        return  self.user.username + " order"


class ShippingDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    email = models.EmailField(max_length=255,null=True)
    fullname = models.CharField(max_length=120)
    contactno = models.CharField(max_length=10)
    address = models.TextField()
    CITYCHOICE = (
        ('surat','Surat'),
        ('ahmedabad','Ahmedabad'),
        ('vadodara','Vadodara'),
    )
    city = models.CharField(choices=CITYCHOICE,max_length=9)
    STATECHOICE = (
        ('gujarat','Gujarat'),
        ('mp','MP')
    )
    state = models.CharField(choices=STATECHOICE,max_length=7)
    zipcode = models.CharField(max_length=6)


    def __str__(self):
        return self.user.username + "  shippingdetails"


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0)

    @property
    def get_per_product_total(self):
        total = self.quantity * self.product.price
        return total


