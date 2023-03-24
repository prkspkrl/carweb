from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('car_title',)}

admin.site.register(Car,CarAdmin)


