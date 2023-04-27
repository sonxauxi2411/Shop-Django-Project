from django.db import models
from django.contrib.auth.models import User

class Products (models.Model):
    title =  models.CharField(max_length=225)
    picture = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=8, decimal_places=1)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
    
    def __str__(self) :
        return self.title
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title} added by {self.user.username} on {self.date_added}"
    
   