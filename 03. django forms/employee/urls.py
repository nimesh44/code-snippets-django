from django.urls import path
from . import views

urlpatterns =[
            path('',views.home,name="home"),
            path('home/',views.home,name="home"),
            path('employee/',views.employee,name="employee-home"),
            path('about/',views.about,name="about"),
            path('contact/',views.contact,name="contact"),
]
