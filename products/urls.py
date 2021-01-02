from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    ShoppingFormUpdate,
    ShoppingFormDelete
)

urlpatterns = [
    path("",views.home,name="homepage"),
    path("checkout",views.checkout,name="checkoutpage"),
    path('update/<int:pk>',ShoppingFormUpdate.as_view(),name="update-shippingform"),
    path('delete/<int:pk>',ShoppingFormDelete.as_view(),name="delete-shippingform"),
    path('process_order', views.processOrder, name="process_order"),
    path("cart",views.cart,name="cartpage"),
    path('updatecart', views.updatecart, name="updatecart"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)