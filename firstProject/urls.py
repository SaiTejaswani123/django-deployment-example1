from django.urls import url
from firstApp import views

urlpatterns=[
path('',views.index,name="index"),
]
