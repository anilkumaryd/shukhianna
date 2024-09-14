from django.shortcuts import render,redirect
#for image access from model
from . models import Product,MainCategory,SubCategory


# Create your views function base here.
def home(request):
    img_data=Product.objects.all()
    img_data=img_data[::-1] ## use for latest product add on
    return render(request,"index.html",{'img_data_value':img_data})

#shop page
def product(request,mc,sc):
    img_data=Product.objects.all()
    img_data=img_data[::-1]
    maincat=MainCategory.objects.all()
    subcat=SubCategory.objects.all()
    return render(request,"product.html",{'img_data_value':img_data,"Maincat":maincat,"Subcat":subcat})

def OrganicSpices(request,mc,sc):
    img_data=Product.objects.all()
    img_data=img_data[::-1]
    maincat=MainCategory.objects.all()
    subcat=SubCategory.objects.all()
    return render(request,"product.html",{'img_data_value':img_data,"Maincat":maincat,"Subcat":subcat})

def NewOrganicMasala(request,mc,sc):
    img_data=Product.objects.all()
    img_data=img_data[::-1]
    maincat=MainCategory.objects.all()
    subcat=SubCategory.objects.all()
    return render(request,"product.html",{'img_data_value':img_data,"Maincat":maincat,"Subcat":subcat})

def PulsesFlour(request,mc,sc):
    img_data=Product.objects.all()
    img_data=img_data[::-1]
    maincat=MainCategory.objects.all()
    subcat=SubCategory.objects.all()
    return render(request,"product.html",{'img_data_value':img_data,"Maincat":maincat,"Subcat":subcat})

def OrganicMisc(request,mc,sc): 
    img_data=Product.objects.all()
    img_data=img_data[::-1]
    maincat=MainCategory.objects.all()
    subcat=SubCategory.objects.all()
    return render(request,"product.html",{'img_data_value':img_data,"Maincat":maincat,"Subcat":subcat})

def OrganicsOil(request,mc,sc):
    img_data=Product.objects.all()
    img_data=img_data[::-1]
    maincat=MainCategory.objects.all()
    subcat=SubCategory.objects.all()
    return render(request,"product.html",{'img_data_value':img_data,"Maincat":maincat,"Subcat":subcat})

