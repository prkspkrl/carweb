from django.urls import path
from . import views


urlpatterns = [
    path('', views.carlist, name= 'carlist'),
    path('<slug:car_slug>/', views.car_detail, name= 'car_detail'),

]

