
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home,name='homepage'),
    path('form/', views.form,name='Contact_form'),
    
]
