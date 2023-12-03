from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('experiencia/', views.experiencia),
    path('servicios/', views.servicios),
    path('contacto/', views.contacto)
]