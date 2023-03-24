from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cardetail', views.cardetail, name='cardetail'),
    # path('carlist', views.carlist, name='carlist'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact/', include('contact.urls')),
    path('cars/', include('cars.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
