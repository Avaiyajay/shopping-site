from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from django.http import JsonResponse
import json
from django.contrib import messages
from .models import *
from .forms import ShippingForm
from django.views.generic import (
    UpdateView,
    DeleteView
)
# Create your views here.

def home(request):
    obj = Product.objects.all()
    context = {
        "obj":obj
    }
    return render(request,"home.html",context)




class ShoppingFormUpdate(UpdateView):
    queryset = ShippingDetail.objects.all()
    template_name='shippingdetail_update.html'
    form_class = ShippingForm
    success_url = '/checkout'

class ShoppingFormDelete(DeleteView):
    template_name = 'shippingdetail_delete.html'
    queryset = ShippingDetail.objects.all()
    form_class = ShippingForm

    def get_success_url(self):
        return reverse('checkoutpage')



def checkout(request):
    form = ShippingForm()
    if request.user.is_authenticated:
        orderitems,created = Order.objects.get_or_create(user = request.user,completed=False)
        cartitems = Cart.objects.filter(user = request.user,order = orderitems)
        forms = ShippingDetail.objects.filter(user=request.user)
    else:
        cart = json.loads(request.COOKIES['cart'])
        cartitems = []
        sum = 0
        for i in cart:
            ordertotal = 0 
            product = Product.objects.get(id = i)
            ordertotal  += cart[i]['quantity'] * (product.price)
            sum += ordertotal
            item = {
                'quantity' : cart[i]['quantity'],
                'get_per_product_total' : ordertotal,
                'product' : {
                    'id' : i,
                    'name' : product.name,
                    'price' : product.price,
                    }
                }
            cartitems.append(item)
        orderitems = {
            'get_total_order_price' : sum
        }
        forms = []
    context = {
        'objects': cartitems,
        'order': orderitems,
        'form':form,
        'forms':forms
    }
    return render(request,"checkout.html",context)


def processOrder(request):
    print("it comes here and go there")
    data = json.loads(request.body)
    form = data['form']
    total = data['orderdata']['total']
    if request.user.is_authenticated:
        order,created = Order.objects.get_or_create(user =  request.user,completed = False)

        if total == order.get_total_order_price:
            order.completed = True
            order.needshipping = True
            print("done")
        order.save()

        fullname = form['fullname']
        contactno = form['contactno']
        address = form['address']
        city = form['city']
        state = form['state']
        zipcode = form['zipcode']
        email = form['email']
        object = ShippingDetail.objects.create(user=request.user, order=order, fullname=fullname, email=email,
                                               contactno=contactno, address=address, city=city, state=state,
                                               zipcode=zipcode)
        object.save()
    data = json.loads(request.body)

    cart = json.loads(request.COOKIES['cart'])
    form = data['form']
    total = data['orderdata']['total']
    cartitems = []
    sum = 0
    for i in cart:
        ordertotal = 0
        product = Product.objects.get(id=i)
        ordertotal += cart[i]['quantity'] * (product.price)
        sum += ordertotal
        item = {
            'quantity': cart[i]['quantity'],
            'get_per_product_total': ordertotal,
            'product': {
                'id': i,
                'name': product.name,
                'price': product.price,
            }
        }
        cartitems.append(item)

        if total == sum:
            pass
    orderitems = {
        'get_total_order_price': sum
    }
    forms = []
    return JsonResponse("Order successfully created",safe=False)


def updatecart(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        productid = data['productid']
        action = data['action']
        product = Product.objects.get(id = productid)
        user = request.user
        order,created = Order.objects.get_or_create(user = user,completed=False)
        cart,created = Cart.objects.get_or_create(product = product,user = user,order=order)

        if action == "add":
            cart.quantity += 1
        if action == "remove":
            cart.quantity -= 1

        cart.save()

        if cart.quantity <= 0:
            cart.delete()

        return JsonResponse("item added successfully",safe=False)

def cart(request):
    if request.user.is_authenticated:
        order,created = Order.objects.get_or_create(user = request.user,completed=False)
        orderitems = Cart.objects.filter(user = request.user,order = order)
    # else:
    #     messages.info(request,"login first then you can see cart")
    #     return redirect("login")
    else:
        cart = json.loads(request.COOKIES['cart'])
        orderitems = []
        sum = 0
        for i in cart:
            ordertotal = 0
            product = Product.objects.get(id = i)
            ordertotal  += cart[i]['quantity'] * (product.price)
            sum += ordertotal
            item = {
                'quantity' : cart[i]['quantity'],
                'get_per_product_total' : ordertotal,
                'product' : {
                    'id' : i,
                    'ImageUrl' : product.ImageUrl,
                    'price' : product.price,
                    }
                }
            orderitems.append(item)
        order = {
            'get_total_order_price' : sum
        }

    context = {
        'objects': orderitems,
        'order': order
    }
    return render(request,"cartpage.html",context)



