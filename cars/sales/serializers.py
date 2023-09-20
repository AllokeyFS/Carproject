from rest_framework import serializers
from .models import Cars, CarsColor, CarsBrand, CarsModel, Country
from .models import Motorcycle, MotorcycleBrand, MotorcycleModel, CarPart


class CarsSerializer(serializers.ModelSerializer):
    # car_name = serializers.CharField(source='cars.brand.name')
    cars_model = serializers.CharField(source='cars.model')
    color_name = serializers.CharField(source='colors.color')
    country_name = serializers.CharField(source='country.name')
    class Meta:
        model = Cars
        fields = ('id', 'cars_model', 'year', 'currency', 'price', 'mileage', \
                'color_name', 'kpp', 'wd', 'steering_wheel', 'vehicle_type', 'carcase', 'fuel', 'state',\
                'vin', 'engine_volume', 'country_name', 'description', )

    def create(self, validated_data):
        # cars_brand = validated_data.pop('cars').get('brand.name')
        # brand = CarsBrand.objects.get(name=cars_brand)
        cars_model = validated_data.pop('cars').get('model')
        model = CarsModel.objects.get(model=cars_model)
        cars_color = validated_data.pop('colors').get('color')
        color = CarsColor.objects.get(color=cars_color)
        cars_country = validated_data.pop('country').get('name')
        country = Country.objects.get(name=cars_country)
        cars = Cars.objects.create(cars=model, colors=color, country=country)
        return cars

class CarsColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsColor
        fields = ('id','color', )

class CarsBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsBrand
        fields = ('id', 'name')

class CarsModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    class Meta:
        model = CarsModel
        fields = ('id', 'brand_name', 'model', )

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class MotorcycleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorcycleBrand
        fields = ('id', 'name')

class MotorcycleModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    class Meta:
        model = MotorcycleModel
        fields = ('id', 'brand_name', 'model', )

class MotorcycleSerializer(serializers.ModelSerializer):
    # motorcycle_name = serializers.CharField(source='motorcycle.brand.name')
    motorcycle_model = serializers.CharField(source='motorcycle.model')
    color_name = serializers.CharField(source='color.color')
    country_name = serializers.CharField(source='country.name')
    class Meta:
        model = Motorcycle
        fields = ('id','motorcycle_model', 'color_name', 'country_name', 'year', \
                'currency', 'price', 'mileage', 'vehicle_type', \
                'kpp', 'fuel', 'state', 'vin', 'engine_volume',\
                'description', 'publication_date', )
        
    def create(self, validated_data):
        motorcycle_model = validated_data.pop('motorcycle').get('model')
        model = MotorcycleModel.objects.get(model=motorcycle_model)
        motorcycle_color = validated_data.pop('color').get('color')
        color = CarsColor.objects.get(color=motorcycle_color)
        motorcycle_country = validated_data.pop('country').get('name')
        country = Country.objects.get(name=motorcycle_country)
        motorcycle = Motorcycle.objects.create(motorcycle=model, color=color, country=country)
        return motorcycle
    
class CarPartSerializer(serializers.ModelSerializer):
    carpart = serializers.CharField(source='car.model')
    class Meta:
        model = CarPart
        fields = ('id', 'name', 'carpart', 'year', 'price', 'state', )