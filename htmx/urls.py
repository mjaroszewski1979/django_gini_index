from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gini/', views.gini, name='gini'),
    path('cpi/', views.cpi, name='cpi'),
]