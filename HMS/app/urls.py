"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app import views

urlpatterns = [
   path('',views.show,name='main'),
   path('checklogin/',views.checklogin,name='checklogin'),
   path('home/',views.home,name='home'),
   path('addp/',views.addp,name='addp'),
   path('save/',views.savep,name='savep'),
   path('addd/', views.addd, name='addd'),
   path('saved/',views.saved,name='saved'),
   path('addt/',views.addt,name='addt'),
   path('savet/', views.savet, name='savet'),
   path('addap/',views.addap,name='addap'),
   path('saveap/',views.saveap,name='saveap'),
   path('addac/',views.addc,name='addc'),
   path('savedc/',views.savedc,name='savedc'),
   path('viewp',views.viewp,name='viewp'),
   path('up',views.up,name='up'),
   path('saveup/',views.saveup,name='saveup'),
   path('delp/',views.delp,name='delp'),
   path('viewd',views.viewd,name='viewd'),
   path('updated/',views.updated,name='updated'),
   path('saveupdatedoctor/',views.saveupdatedoctor,name='saveupdatedoctor'),
   path('deld/',views.deld,name='deld'),
   path('viewt/',views.viewt,name='viewt'),
   path('delt/',views.delt,name='delt'),
   path('viewapt/',views.viewapt,name='viewapt'),
   path('delapt/',views.delapt,name='delapt'),
   path('viewdc/',views.viewdc,name='viewdc'),
   path('deldc/',views.deldc,name='deldc')
]
