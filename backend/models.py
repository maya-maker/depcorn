from django.db import models



class Register(models.Model):
    username = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/vegetable')



class Cart(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/vegetable')



class Order(models.Model):
    product_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    quantity = models.IntegerField()
    amount = models.IntegerField()


