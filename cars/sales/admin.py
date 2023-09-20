from django.contrib import admin
from .models import Cars, CarsColor, CarsBrand, CarsModel, Country
from .models import Motorcycle, MotorcycleBrand, MotorcycleModel, CarPart

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cars', 'year', 'currency', 'price', 'mileage', 'colors', 'kpp', 'wd', 'steering_wheel', \
                    'vehicle_type','carcase', 'fuel', 'state', 'vin', 'engine_volume', 'description', )
    list_filter = ('year', 'colors', 'kpp', 'wd', 'vehicle_type', 'carcase', 'fuel', 'state', 'engine_volume')
    search_fields = ('cars__brand_name', 'cars__model', 'year', 'price', 'mileage' )

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )

@admin.register(CarsColor)
class CarsColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color',)
    search_fields = ('color', )

@admin.register(CarsBrand)
class CarsBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    

@admin.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model',)
    list_filter = ('brand', )
    search_fields = ('brand__name', )



@admin.register(MotorcycleBrand)
class MotorcycleBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    

@admin.register(MotorcycleModel)
class MotorcycleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model',)
    list_filter = ('brand', )
    search_fields = ('brand__name', )

@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'motorcycle', 'color', 'country', 'year', \
                'currency', 'price', 'mileage', 'vehicle_type', \
                'kpp', 'fuel', 'state', 'vin', 'engine_volume', 'country',\
                'description', 'publication_date', )
    list_filter = ('year', 'color', 'kpp', 'vehicle_type', 'fuel', 'state', 'engine_volume')
    search_fields = ('motorcycle__brand_name', 'motorcycle__model', 'year', 'price', 'mileage' )

@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'car', 'year', 'price', 'state', )