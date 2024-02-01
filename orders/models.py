from django.db import models
from customers.models import Customer
from products.models import Product
# Cart
class CartOrder(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRM=1
    ORDER_REJECT=-1
    ORDER_PROCESS=2
    ORDER_DELIVERED=3
    STATUS_CHOICE=((ORDER_DELIVERED,'ORDER_DELIVERED'),
                   (ORDER_PROCESS,"ORDER_PROCESS"),
                   (ORDER_REJECT,"ORDER_REJECT"))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders',null=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(CartOrder,on_delete=models.CASCADE,related_name='added_items')
