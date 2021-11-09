# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 23:53:20 2021

@author: SAYANTAN PC
"""
from django.urls import path,include
from calc import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('add',views.add,name='add')
]
