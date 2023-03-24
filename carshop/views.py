from django.shortcuts import render
from cars.models import Car

def home(request):
    featured_car = Car.objects.filter(is_featured = True)
    all_car = Car.objects.all()
    context = {
        'featured_car' : featured_car,
        'all_car' : all_car,
    }
    return render(request,'home.html', context)

def cardetail(request):
    return render(request, 'pages/car-details.html')

def services(request):
    return render(request, 'pages/services.html')

def about(request):
    return render(request, 'pages/about.html')
