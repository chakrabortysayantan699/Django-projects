from django.urls import path,include
from travello import views

urlpatterns=[
          path('',views.travel,name='travel'),
          path('message',views.message,name='message')
]