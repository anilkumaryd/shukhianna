from django.db import models
from decimal import Decimal

# Create your models here.
## MainCategory
class MainCategory(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.name
## Subcategory
class SubCategory(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    maincat = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    baseprice = models.DecimalField(max_digits=10, decimal_places=2)  # Allows up to 10 digits, with 2 decimal places
    discount = models.DecimalField(max_digits=5, decimal_places=2)    # If it's a percentage or absolute amount
    finalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    discription = models.TextField()
    stock = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now=True)
    pic1 = models.ImageField(upload_to="images/", blank=True, null=True)
    pic2 = models.ImageField(upload_to="images/", blank=True, null=True)
    pic3 = models.ImageField(upload_to="images/", blank=True, null=True)
    pic4 = models.ImageField(upload_to="images/", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate the final price based on base price and discount
        if self.discount:
            self.finalPrice = self.baseprice * (Decimal('1.00') - (self.discount / Decimal('100.00')))
        else:
            self.finalPrice = self.baseprice
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)+" "+self.name
    

conatctstatus = ((0,"Active"),(1,"Done"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.IntegerField(choices=conatctstatus,default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.subject



