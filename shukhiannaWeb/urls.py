"""
URL configuration for shukhiannaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shukhiannaApp import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('product/<str:mc>/<str:sc>/',views.product),
    path('OrganicSpices/<str:mc>/<str:sc>/',views.OrganicSpices),

    path('NewOrganicMasala/<str:mc>/<str:sc>/',views.NewOrganicMasala),
    path('PulsesFlour/<str:mc>/<str:sc>/',views.OrganicSpices),
    path('OrganicMisc/<str:mc>/<str:sc>/',views.OrganicMisc),
    path('OrganicsOil/<str:mc>/<str:sc>/',views.OrganicsOil),
    path('contact/',views.contactpage),
    path('terms_and_conditons/',views.Termspage),
    path('privacy_policy/',views.Privacypage),
    path('About/',views.Aboutpage),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
