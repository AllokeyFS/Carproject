import django_filters
from django.shortcuts import render
from .serializers import CarsSerializer, CarsBrandSerializer, CountrySerializer
from .serializers import MotorcycleBrandSerializer, MotorcycleModelSerializer, MotorcycleSerializer, CarPartSerializer
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Cars, CarsBrand, Country, Motorcycle, MotorcycleBrand, MotorcycleModel, CarPart
from datetime import datetime, timedelta
from django.utils import timezone

class CarsViewSets(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_fields = ('cars__brand__name','cars__model', 'year', 'colors__color', 'kpp', 'wd', 'vehicle_type', 'carcase', 'fuel', 'state', 'engine_volume' )

class NewCarsListAPI(ListAPIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        return Cars.objects.filter(year__gte=2021)

class CarsBrandListAPI(ListAPIView):
    serializer_class = CarsBrandSerializer

    def get_queryset(self):
        return CarsBrand.objects.all()
    
class CountryListAPI(ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all()


def welcome_page(request):
    return render(request, 'html/index.html')


class MotorcycleBrandListAPI(ListAPIView):
    serializer_class = MotorcycleBrandSerializer

    def get_queryset(self):
        return MotorcycleBrand.objects.all()

class MotorcycleModelListAPI(ListAPIView):
    serializer_class = MotorcycleModelSerializer

    def get_queryset(self):
        return MotorcycleModel.objects.all()

class MotorcycleViewSets(viewsets.ModelViewSet):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_fields = ('motorcycle__brand__name','motorcycle__model', 'year', 'color__color', 'kpp', 'vehicle_type', 'fuel', 'state', 'engine_volume' )


class CarsAdCounter(ListAPIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        return Cars.objects.count()
    
class MotoAdCounter(ListAPIView):
    serializer_class = MotorcycleSerializer

    def get_queryset(self):
        return Motorcycle.objects.count()
    
class CarPartViewSets(viewsets.ModelViewSet):
    queryset = CarPart.objects.all()
    serializer_class = CarPartSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_fields = ('name', 'car__brand__name','car__model', 'year', 'price', 'state', )