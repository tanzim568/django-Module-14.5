
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='homepage'),
    path('form/', views.djangoForm,name='formpage'),
    path('about/', views.about,name='aboutpage'),
    path('models/', views.models,name='modelpage'),
    path('delete/<int:roll>', views.delete,name='deletedata'),
    path('modelform/', views.djangoModel,name='modelform'),
    
]