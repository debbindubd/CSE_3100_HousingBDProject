from django.urls import path
from userapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('properties', views.properties, name='properties'),
    path('services', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/',views.form, name='form'),
    # path('logout/', views.logout_user, name='logout_user'),
]