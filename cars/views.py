from django.shortcuts import render, redirect
from .models import Car
from django.shortcuts import get_object_or_404

# Create your views here.
def carlist(request):
    allcar = Car.objects.all()
    context = {
        'allcar' : allcar,
    }
    return render(request, 'pages/carlist.html', context)

def car_detail(request,car_slug):
    car_slugs = get_object_or_404(Car, slug=car_slug)
    context ={
        'car_slugs':car_slugs,
    }
    # print(car_slugs)

    return render(request,'pages/car-details.html',context)

