from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Showes'),(3,'Cloth'))
    pname=models.CharField(max_length=20,verbose_name='Product Name')
    price=models.IntegerField()
    pdetail=models.CharField(max_length=300,verbose_name='Product Detail')
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')

    def __str__(self):
        return self.pdetail

class Cart(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)  
    amt=models.IntegerField()  