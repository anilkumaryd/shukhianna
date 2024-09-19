from django.shortcuts import render,redirect
from django.contrib import messages
#for image access from model
from . models import *


# Create your views function base here.
def home(request):
    img_data=Product.objects.all()
    img_data=img_data[::-1] ## use for latest product add on
    return render(request,"index.html",{'img_data_value':img_data})

#shop page
def product(request,mc,sc):
    if(mc=="all" and sc=="all"):
      img_data=Product.objects.all()
      img_data=img_data[::-1]
    elif(mc!="all" and sc=="all"):
        img_data=Product.objects.filter(maincat=MainCategory.objects.get(name=mc))
        val=img_data.values()
        print("va----------",val)

    maincat=MainCategory.objects.all()
    subcat=SubCategory.objects.all()
    return render(request,"product.html",{'img_data_value':img_data,"Maincat":maincat,"Subcat":subcat,
                                          "MC":mc,
                                          "SC":sc
                                          })

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

def contactpage(Request):
    if(Request.method=="POST"):
        c = Contact()
        c.name = Request.POST.get("name")
        c.email = Request.POST.get("email")
        c.phone = Request.POST.get("phone")
        c.subject = Request.POST.get("subject")
        c.message = Request.POST.get("message")
        c.save()
        messages.success(Request,"Thanks to Share Your Query With US!! Our Team Will Contact You Soon!!!!")
    return render(Request,"contact.html")

def Termspage(request):
    return render(request,"Terms.html")

def Privacypage(request):
    return render(request,"Privacy.html")

def Aboutpage(request):
     return render(request,"About.html")