from django.urls import path
from .views import CarsViewSets, welcome_page, NewCarsListAPI, CarsBrandListAPI
from .views import CountryListAPI, MotorcycleBrandListAPI, MotorcycleViewSets, MotorcycleModelListAPI
from .views import CarsAdCounter, MotoAdCounter, CarPartViewSets

urlpatterns = [
    path('', welcome_page, name='welcome'),
    path('cars/', CarsViewSets.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('cars/<int:pk>/',CarsViewSets.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
    path('new_auto/',NewCarsListAPI.as_view()),
    path('cars_brand/', CarsBrandListAPI.as_view()),
    path('country/', CountryListAPI.as_view()),
    path('motorcycle/', MotorcycleViewSets.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('motorcycle/<int:pk>/',MotorcycleViewSets.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
    path('motorcycle_brand/', MotorcycleBrandListAPI.as_view()),
    path('motorcycle_model/', MotorcycleModelListAPI.as_view()),
    path('car_ad/', CarsAdCounter.as_view()),
    path('moto_ad/', MotoAdCounter.as_view()),
    path('car_part/', CarPartViewSets.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('car_part/<int:pk>/',CarPartViewSets.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
    
]